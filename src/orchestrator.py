from datetime import datetime
from luis.luis_client import LUIS
from bots.explore_world import Explore_world
from bots.finalization import Finalization
from bots.login import Login
from bots.register import Register
from bots.perfect_trip import PerfectTrip

class TravelAssistant:
    def __init__(self):
        self.finalization = Finalization(self)

    def display_bot_response(self, response):
        print(f"Bot: {response}\n")

    def start_conversation(self):
        greeting = self.get_greeting()
        print(
            f"\nBot: {greeting}! Bem-vindo a \033[1mAeroQuest Navigator\033[0m, meu nome é Aria e sou sua assistente de viagens. Como posso ajudá-lo hoje? 🫡 ✈️\n\n- \033[1mCadastro\n- Login\n- Sua viagem perfeita\n- Desbravar o mundo\033[0m\n"
            )
        user_input = input("You: ")
        print("\n")
        self.start_conversation_response_option(user_input)

    def get_greeting(self):
        current_hour = datetime.now().hour

        if 6 <= current_hour < 12:
            return "Bom dia"
        elif 12 <= current_hour < 18:
            return "Boa tarde"
        else:
            return "Boa noite"

    def start_conversation_response_option(self, option):
        analysis_result = LUIS().analyze_language(text=option)
        bot_instance = self.get_bot_instance(analysis_result['topIntent'])

        if bot_instance:
            bot_instance.introduction()
        else:
            self.default_handler()

    def get_bot_instance(self, analysis_result):
        bots = {
            "exploretheworld": Explore_world(self),
            "login": Login(),
            "register": Register(),
            "perfecttrip": PerfectTrip(self),
            "gotoout": Finalization(self),
        }
        return bots.get(analysis_result)

    def default_handler(self):
        print("Desculpa, não consegui entender. 🫤")
        self.start_conversation()

    def run(self):
        while True:
            user_init = input("You: ")
            print("\n")
            analysis_result = LUIS().analyze_language(text=user_init)
            bot_instance = self.get_bot_instance(analysis_result['topIntent'])
            if analysis_result == "gotoout":
                bot_instance.introduction()
            self.start_conversation()

if __name__ == "__main__":
    main_handler = TravelAssistant()
    main_handler.run()
