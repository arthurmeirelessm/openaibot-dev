import time
import requests
from luis.luis_client import LUIS
from openAI.client import GPT3ChatClient
from speech.client import Speech


class Explore_world:
    def __init__(self):
        self.luis = LUIS()
        self.openAI = GPT3ChatClient()
        self.speech = Speech()

    def introduction(self):
        print(
            "Muito bem, vamos explorar o mundo juntos! Conte-me ou pergunte-me através da sua fala sobre um país ou cultura que te intriga! 😊🌍"
        )
        self.call_speech()       
        
    def call_speech(self):
        time.sleep(3)

        user_input = self.speech.TranscribeCommand()
        
        luis_intent = self.luis.analyze_language(user_input)
        
        intent_actions = {"exploretheworld": lambda: self.explore_culture(user_input)}
        intent_actions.get(luis_intent, self.handle_unrecognized_intent)()

            
    def handle_unrecognized_intent(self):
        print("Desculpe, não consegui identificar sua intenção. 🫤\nMe pergunte ou me conte uma curiosidade de algum lugar do mundo.")
        self.call_speech()

    def explore_culture(self, user_input):
        print("passei")
        self.openAI.generate_response(user_input)
