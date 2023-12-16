from authetication.backend import Backend 
from luis.luis_client import LUIS

class Register:
    def __init__(self):
        self.backend = Backend()
        self.luis = LUIS()
        
        
    def introduction(self):
        print("Bem-vindo ao meu processo de cadastro! Para começar, preciso coletar alguns dados seus.\n")
            
        name = input("Digite seu nome completo: ")
            
            
        luis_intent_name = self.luis.analyze_language(name)
            
        if luis_intent_name["topIntent"] == "user_register" and luis_intent_name["categories"] == "name":
            email = input("Digite seu e-mail: ")
            luis_intent_email = self.luis.analyze_language(email)
            
            if luis_intent_email["topIntent"] == "userRegister" and luis_intent_email["categories"] == "email":
                self.backend.register_user(name, email)
                return

        self.name_not_recognized()
        self.email_not_recognized()
        

    def name_not_recognized(self):
        print("Desculpe, o formato do nome inserido não é reconhecido. Por favor, insira um nome válido.")

    def email_not_recognized(self):
        print("Desculpe, o formato do e-mail inserido não é reconhecido. Por favor, insira um e-mail válido.")

        
        
