from luis.luis_client import LUIS
from authetication.backend import Backend
from bots.purchase_flow import PurchaseFlow

class Register:
    def __init__(self, travel_assistant):
        self.travel_assistant = travel_assistant
        self.backend = Backend()
        self.purchase_flow = PurchaseFlow(travel_assistant)
        self.luis = LUIS()
        
    def introduction(self):
        print("Bot: Bem-vindo ao meu processo de cadastro! Para começar, preciso coletar alguns dados seus.\n")
        self.name_input()
        
    def name_input(self): 
        name = input("\033[1mBot: Digite seu nome completo =>\033[0m ")
        print("\n")
        luis_intent_name = self.luis.analyze_language(name)
        if luis_intent_name["topIntent"] == "user_register" and luis_intent_name["categories"] == "name":
            self.email_input(name)
        else:
            self.name_not_recognized()
    
    def email_input(self, name):
        email = input("\033[1mBot: Digite seu e-mail =>\033[0m ")
        print("\n")
        luis_intent_email = self.luis.analyze_language(email)
        
        if luis_intent_email["topIntent"] == "user_register" and luis_intent_email["categories"] == "email":
            self.purchase_flow.introduction(email)
        else:
            self.email_not_recognized(name)

    def name_not_recognized(self):
        print("Bot: Desculpe, o formato do nome inserido não é reconhecido. Por favor, insira um nome válido. 😓\n")
        self.name_input()

    def email_not_recognized(self, name):
        print("Bot: Desculpe, o formato do e-mail inserido não é reconhecido. Por favor, insira um e-mail válido. 😓\n")
        self.email_input(name)
