# login.py
from authetication.backend import Backend
from bots.purchase_flow import PurchaseFlow
from bots.finalization import Finalization
import re

class Login:
    def __init__(self, travel_assistant):
        self.travel_assistant = travel_assistant
        self.backend = Backend() 
        self.purchase_flow = PurchaseFlow()  
    
    def introduction(self):
        print("\nDigite seu email cadastrado para fazer login.")
        user_input = input("You: ")
        verifyemail = self.backend.get_user_data(user_input)
        if verifyemail:
            self.purchase_flow.introduction()
        else:
            print("Usuário não encontrado.\n")
            print("Tentar novamente? ")
            self.ask_if_you_want_to_register(user_input)
            
    def ask_if_you_want_to_register(self, user_input):
            print("\nBot: \033[1m1 - Sim\n2 - Não, voltar ao menu inicial\033[0m\n")
            user_input = input("You: ")
            print("\n")
            if re.search(r"\b(sim|claro|quero|1)\b", user_input, flags=re.IGNORECASE):
               self.introduction()
            elif re.search(r"\b(n[ãa]o|nopes|nada|2)\b", user_input, flags=re.IGNORECASE):
                self.travel_assistant.start_conversation()
        
