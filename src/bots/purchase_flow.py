from openAI.client import GPT3ChatClient
from vision.ocr import PDFTextExtractor
from bots.finalization import Finalization
from luis.luis_client import LUIS
import json
import config
import re
from authetication.notification import EmailSender
import time


class PurchaseFlow:
    def __init__(self, travel_assistant):
        self.travel_assistant = travel_assistant
        self.finalization = Finalization(travel_assistant)
        self.openai = GPT3ChatClient()
        self.notification = EmailSender()
        self.luis = LUIS()
        self.ocr = PDFTextExtractor(file_path=r"C:\bot-openAI\src\vision\kb", base_file="tickets.pdf")    
        
    def introduction(self, email):
        print("Bot: Cadastro feito com sucesso! ✅\n")
        self.firt_interation(email)
    
    def firt_interation(self, email):
        print("Bot: Nessa seção você poderá realizar compras de passagens aéreas internacionais.\n")
        print("Bot: Para onde deseja ir?\nIremos listar os próximos destinos disponíveis.\n")
        user_input = input("You: ")
        self.openai_in_OCR_Integration(user_input, email)
        
    def openai_in_OCR_Integration(self, user_input, email):
        if self.verify_intent(user_input) is None:
            read_result = self.ocr.extract_text_from_pdf()
            prompt_optimization = f"Input: {user_input}. Traga informações SOMENTE da cidade, disponibilidade e valor em um formato organizado de texto com tópicos numericos que dão match com a cidade ou país dito em 'input' de acordo com o que tem essa base de conhecimento aqui = {read_result}"
            response_text = self.openai.generate_response_text(prompt_optimization)
            print(response_text)
            print("\nBot: Alguma opção de passagem aérea disponível mais lhe agradou?\n")
            second_input = input("You: ")
            if re.search(r"\b(n[ãa]o|nopes|nada|nenhuma|nenhuma opção|deixa pra depois)\b", second_input, flags=re.IGNORECASE):
                self.finalization.introduction()
            print("\n")
            self.ask_about_choice(second_input, response_text, email)
        
        
    def ask_about_choice(self, second_input, response_text, email):
        if self.verify_intent(second_input) is None:
            prompt_optimization = f"Input: {second_input}.  Traga a opção escolhida em 'input' semelhante a essas opções aqui {response_text}. Por fim, agradeça o contato."
            response_text = self.openai.generate_response_text(prompt_optimization)
            print(response_text)
            print("\nBot: Tudo certo!? Em breve você receberá um email para detalhes de pagamento.")
            self.notification.send_purchase_details(email)
            self.ask_more_questions()
            
    
    def ask_more_questions(self):
            print("\nBot: \033[1mDeseja ver mais passagens?\n1 - Sim\n2 - Não\n3 - Voltar a opção inicial\033[0m\n")
            user_input = input("You: ")
            print("\n")
            if re.search(r"\b(sim|claro|quero|s|1)\b", user_input, flags=re.IGNORECASE):
                self.firt_interation()
            elif re.search(r"\b(n[ãa]o|nopes|nada|finalizar2)\b", user_input, flags=re.IGNORECASE):
                self.finalization.introduction()
            else:
                self.finalization.travelAssistant.start_conversation()
                
    def verify_intent(self, user_input):
        luis_intent = self.luis.analyze_language(user_input)    
        intent_mapping = {
        "gotoout": self.finalization.introduction,
        "back": self.travel_assistant.start_conversation
        }
    
        top_intent = luis_intent.get('topIntent')
        action = intent_mapping.get(top_intent, None)
        if action:
            return action()
        
    def handle_unrecognized_intent(self):
        print("\nBot: Desculpe, não consegui identificar sua intenção. 🫤")
        self.firt_interation()