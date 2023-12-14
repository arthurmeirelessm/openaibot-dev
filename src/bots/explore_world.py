import time
import requests
from luis.luis_client import LUIS
from openAI.client import GPT3ChatClient
from speech.client import Speech
from bots.finalization import Finalization
import re


class Explore_world:
    def __init__(self, travel_assistant):
        self.luis = LUIS()
        self.openAI = GPT3ChatClient()
        self.speech = Speech()
        self.finalization = Finalization(travel_assistant)

    def introduction(self):
        print(
            "Bot: Muito bem, vamos explorar o mundo juntos! Conte-me ou pergunte-me através da sua fala sobre um país ou cultura que te intriga! 😊🌍"
        )
        self.call_speech()

    def call_speech(self):
        time.sleep(3)

        user_input = self.speech.TranscribeCommand()

        luis_intent = self.luis.analyze_language(user_input)

        intent_actions = {
            "gotoout": self.finalization.introduction,
            "exploretheworld": lambda: self.explore_culture(user_input),
        }
        intent_actions.get(luis_intent, self.handle_unrecognized_intent)()
        self.ask_more_questions(luis_intent)

    def handle_unrecognized_intent(self):
        print(
            "Desculpe, não consegui identificar sua intenção. 🫤\nMe pergunte ou me conte uma curiosidade de algum lugar do mundo."
        )
        self.call_speech()

    def explore_culture(self, user_input):
        self.openAI.generate_response(user_input)

    def ask_more_questions(self, luis_intent):
        if luis_intent == "exploretheworld":
            print("Deseja fazer outra pergunta?\n1 - Sim\n2 - Não\n3 - Voltar a opção inicial")
            user_input = input("You: ")
            if re.search(r"\b(sim|claro|quero)\b", user_input, flags=re.IGNORECASE):
                self.call_speech()
            elif re.search(r"\b(n[ãa]o|nopes|nada)\b", user_input, flags=re.IGNORECASE):
                self.finalization.introduction()
            else:
                self.finalization.travelAssistant.start_conversation()
