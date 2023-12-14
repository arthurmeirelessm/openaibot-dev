import re

class Finalization:
    def __init__(self, travel_assistant):
        self.travelAssistant = travel_assistant
        
    def introduction(self):
        print("Bot: Deseja finalizar?\n1 - Sim\n2 - Não\n3 - Voltar a opção inicial")
        user_input = input("You: ")
        if re.search(r'\b(sim|claro|quero)\b', user_input, flags=re.IGNORECASE):
            self.send_finalization_message()
        elif re.search(r'\b(n[ãa]o|nopes|nada)\b', user_input, flags=re.IGNORECASE):
            return 'nao'
        else:
            self.travelAssistant.start_conversation()
    
    def send_finalization_message(self):
        print("Obrigado por usar nosso serviço! Até logo. 😊")