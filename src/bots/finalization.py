import re
import sys
from analysis.sentiment_client import SentimentAnalyzer

class Finalization:
    def __init__(self, travel_assistant):
        self.travelAssistant = travel_assistant
        self.sentiment = SentimentAnalyzer()
        
    def introduction(self):
        print("\nBot: Deseja finalizar?\n\033[1m1 - Sim\n2 - Não, voltar a opção inicial\033[0m\n")
        user_input = input("You: ")
        print("\n")
        if re.search(r'\b(sim|claro|quero|1)\b', user_input, flags=re.IGNORECASE):
            self.faq()
        elif re.search(r'\b(n[ãa]o|nopes|nada|2)\b', user_input, flags=re.IGNORECASE):
            self.travelAssistant.start_conversation()
    
    def faq(self):
        print("\033[1mSua avaliação é importante pra mim! Antes de ir, avalie o meu serviço. Conte-me como foi sua experiência aqui em baixo: 🙏🏻\033[0m\n")
        user_input = input("You: ")
        print("\n")
        documents = [user_input]
        analysis = self.sentiment.analyze_sentiment(documents)
        
        self.finalization_case_good_analysis() if analysis == "positive" else (self.finalization_case_neutral_analysis() if analysis == "neutral" else self.finalization_case_bad_analysis())

    
    def finalization_case_good_analysis(self):
        print("Fico feliz que teve uma experiência satisfatória comigo! Obrigado por escolher nosso serviço. Até logo! 😊")
        sys.exit()
    
    def finalization_case_neutral_analysis(self):
        print("Agradecemos por utilizar nosso serviço. Estou aqui para ajudar. Até logo. 😊")
        sys.exit()
    
    def finalization_case_bad_analysis(self):
        print("Lamentamos que sua experiência não tenha sido satisfatória. 🫤 Faremos o possível para melhorar. Obrigado por usar nosso serviço. Até logo.")
    
        # MANDAR CONTAGENS DE AVALIAÇÕES PRA UM CONTAINER BLOB STORAGE AZURE PARA LOGS E MELHORIA CONTIMUA DO BOT
        
        sys.exit()