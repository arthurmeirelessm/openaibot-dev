# error_messages.py
from bots.finalization import Finalization

class ErrorMessages:
    def __init__(self, finalization, caller):
        self.caller = caller
        self.finalization = finalization
        self.unrecognized_intent_count = 0

    def count_empty_input(self, user_input):
        if not user_input:
            self.unrecognized_intent_count += 1
            if self.unrecognized_intent_count >= 4:
                self.finalization.introduction()
            elif self.unrecognized_intent_count == 3:
                self.deal_with_third_attempt()
            else:
                self.handle_unrecognized_intent()

    def handle_unrecognized_intent(self):
        print(
            "\nDesculpe, não consegui identificar sua intenção. 🫤\nMe pergunte ou me conte uma curiosidade de algum lugar do mundo."
        )
        self.caller.call_speech()

    def deal_with_third_attempt(self):
        print("\nSua intenção não foi reconhecida pela terceira vez. \nCaso queira \033[1mFINALIZAR\033[0m basta me falar também.")
        self.caller.call_speech()
