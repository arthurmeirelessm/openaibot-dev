import time
import requests
from luis.luis_client import LUIS
from openAI.client import GPT3ChatClient
from speech.client import Speech
from bots.finalization import Finalization
from bots.error_messages import ErrorMessages
import re


class Explore_world:
    def __init__(self, travel_assistant):
        self.travel_assistant = travel_assistant
        self.luis = LUIS()
        self.openAI = GPT3ChatClient()
        self.speech = Speech()
        self.finalization = Finalization(travel_assistant)
        self.error = ErrorMessages(self.finalization, self)
        self.unrecognized_intent_count = 0

    def introduction(self):
        print(
            "Bot: Muito bem, vamos explorar o mundo juntos! Conte-me ou pergunte-me através da sua fala sobre um país ou cultura que te intriga! 😊🌍"
        )
        self.call_speech()

    def call_speech(self):
        time.sleep(3)

        user_input = self.speech.TranscribeCommand()
        
        self.error.count_empty_input(user_input)
                            
        luis_intent = self.luis.analyze_language(user_input)
        
        final_input = f"Forneça uma resposta direta e em poucas linhas para essa pergunta: {user_input}"

        intent_actions = {
            "gotoout": self.finalization.introduction,
            "back": self.travel_assistant.start_conversation(),
            "exploretheworld": lambda: self.explore_culture(final_input),
        }
        top_intent = luis_intent['topIntent']
        intent_actions.get(top_intent, self.error.handle_unrecognized_intent)()
        self.ask_more_questions(top_intent)

    def explore_culture(self, user_input):
        self.openAI.generate_response(user_input)

    def ask_more_questions(self, luis_intent):
        if luis_intent == "exploretheworld":
            print("\nBot: Deseja fazer outra pergunta?\n\033[1m1 - Sim\n2 - Não\n3 - Voltar a opção inicial\033[0m\n")
            user_input = input("You: ")
            if re.search(r"\b(sim|claro|quero|1)\b", user_input, flags=re.IGNORECASE):
                self.call_speech()
            elif re.search(r"\b(n[ãa]o|nopes|nada|2)\b", user_input, flags=re.IGNORECASE):
                self.finalization.introduction()
            else:
                self.finalization.travelAssistant.start_conversation()
                
            
