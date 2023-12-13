from datetime import datetime
from luis.luis_client import LUIS
from bots.explore_world import Explore_world
from bots.finalization import Finalization
from bots.login import Login
from bots.register import Register
from bots.perfect_trip import PerfectTrip


class TravelAssistant:
    def __init__(self, main_handler):
        self.main_handler = main_handler

    def display_bot_response(self, response):
        print(f"Bot: {response}\n")

    def start_conversation(self):
        greeting = self.get_greeting()
        print(
            f"Bot: {greeting}! Bem-vindo a ViajeBem Destinos, seu assistente de viagens. Como posso ajudá-lo hoje? 🫡 ✈️\n1 - Desbravar o mundo\n2 - Cadastro\n3 - Login\n4 - Sua viagem perfeita"
        )
        user_input = input("You: ")
        self.main_handler.start_conversation_response_option(user_input)

    def get_greeting(self):
        current_hour = datetime.now().hour

        if 6 <= current_hour < 12:
            return "Bom dia"
        elif 12 <= current_hour < 18:
            return "Boa tarde"
        else:
            return "Boa noite"


class MainHandler:
    def __init__(self):
        self.travel_assistant = TravelAssistant()
        self.luis = LUIS()
        self.bots = {
            "exploretheworld": Explore_world(),
            "login": Login(),
            "register": Register(),
            "perfecttrip": PerfectTrip(),
            "gotoout": PerfectTrip(),  # Se "gotoout" deve ir para a mesma classe que "perfecttrip"
        }

    def start_conversation_response_option(self, option):
        analysis_result = self.luis.analyze_language(text=option)
        bot_instance = self.bots.get(analysis_result)

        if bot_instance:
            bot_instance.minha_funcao_principal()
        else:
            self.default_handler()

    def default_handler(self):
        print("Desculpa, não consegui entender. 🫤")
        self.travel_assistant.start_conversation()

    def run(self):
        while True:
            user_init = input("You: ")
            analysis_result = self.luis.analyze_language(text=user_init)
            if analysis_result == "gotoout":
                self.finalization.minha_funcao_principal()
                break
            self.travel_assistant.start_conversation()


if __name__ == "__main__":
    main_handler = MainHandler()
    main_handler.run()
