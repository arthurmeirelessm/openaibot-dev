import time
from luis.luis_client import LUIS
from speech.client import Speech
from bots.finalization import Finalization
from openAI.client import GPT3ChatClient
from bots.error_messages import ErrorMessages
import re


class PerfectTrip:
    def __init__(self, travel_assistant):
        self.travel_assistant = travel_assistant
        self.luis = LUIS()
        self.speech = Speech()
        self.finalization = Finalization(travel_assistant)
        self.error = ErrorMessages(self.finalization, self)
        self.openAI = GPT3ChatClient()

    def introduction(self):
        print("Bot: Nessa sessão, sou a sua companheira perfeita para planejar a viagem dos seus sonhos! Esolha destinos emocionantes com base nas suas preferências.\n")
        self.introduction_response()
        
    def introduction_response(self):
        print("- \033[1mAtividades de aventura\n- Culinária exclusiva\n- Belezas naturais\n- Atrações culturais\n- Festas\033[0m\n")
        user_input = input("You: ")
        print("\n")
        self.verify_entities(user_input)
        
            
    def call_speech(self):
        time.sleep(4)

        user_input = self.speech.TranscribeCommand()
        
        self.error.count_empty_input(user_input)
        
        luis_intent = self.luis.analyze_language(user_input)
        
        final_input = f"Forneça uma resposta direta e em poucas linhas para essa pergunta: {user_input}"
                
        intent_actions = {
            "gotoout": self.finalization.introduction,
            "perfecttrip": lambda: self.explore_culture(final_input),
            "back": self.travel_assistant.start_conversation  
}
        top_intent = luis_intent['topIntent']
        intent_actions.get(top_intent, self.error.handle_unrecognized_intent)()
        self.ask_more_questions(top_intent)
    
    
    def explore_culture(self, user_input):
        self.openAI.generate_response_speech(user_input)
        
    def intro_adventure_activities(self):
        print("Bot: \033[1mDeseja se aventurar pelo mundo a fora!? Vem comigo.\033[0m🪂🚵\n\nBot: Peça sugestão de lugares que tenha os tipos de atividades radicais do seu interesse.\n\033[1mExemplo: Qual é o melhor país para quem quer se aventurar em trilhas de 4x4 e off-road?\033[0m\n")
    
    def intro_cooking(self):
         print("Bot: \033[1mDescubra o sabor único da culinária exclusiva.\033[0m🌮🍝\n\nBot: Peça sugestão de lugares que tenha os tipos de culinárias exclusivas/exóticas do seu interesse.\n\033[1mExemplo: Estou buscando um destino com culinária exótica asiática. Alguma recomendação?\033[0m\n")
    
    def intro_natural_beauty(self):
         print("Bot: \033[1mExplore a beleza natural deslumbrante.\033[0m🌅⛰️\n\nBot: Peça sugestão de lugares que tenha os tipos de belezas naturais do seu interesse.\n\033[1mExemplo: Pode sugerir um país na América do Sul conhecido por suas paisagens naturais deslumbrantes?\033[0m\n")
    
    def intro_cultural(self):
        print("Bot: \033[1mImmerja-se em experiências culturais inesquecíveis.\033[0m🎎🏯\n\nBot: Peça sugestão de lugares que tenha os tipos de atrações culturais do seu interesse.\n\033[1mExemplo: Qual país tem com a cultura indigina mais forte você me daria de sugestão?\033[0m\n")
    
    def intro_party(self):
         print("Bot: \033[1mEntão prentede viajar para curtir, hein!? rs\033[0m🍸🥳\n\nBot: Peça sugestão de lugares que tenha os tipo de festa do seu interesse.\n\033[1mExemplo: Estou buscando um destino com as melhores festas eletrônicas. Alguma recomendação?\033[0m\n")
    
    
    
    def verify_entities(self, user_input):
        luis_result = self.luis.analyze_language(user_input)
        
        intent_mapping = {
        "gotoout": self.finalization.introduction,
        "back": self.travel_assistant.start_conversation,
        "adventure_activities": self.intro_adventure_activities,
        "cooking": self.intro_cooking,
        "natural_beauty": self.intro_natural_beauty,
        "cultural": self.intro_cultural,
        "party": self.intro_party
        }
        intent = luis_result.get('topIntent') if luis_result.get('topIntent') in intent_mapping else luis_result.get('categories')
        action = intent_mapping.get(intent, self.default_intro)
        action()
        self.call_speech()

    
    def default_intro(self):
        print("\nBot: Desculpe, não consegui identificar sua intenção. 🫤\nEscolha uma das opções listadas.\n")
        self.introduction_response()
    
    def ask_more_questions(self, luis_intent):
        if luis_intent == "perfecttrip":
            print("\nBot: \033[1mDeseja fazer outra pergunta?\n1 - Sim\n2 - Não\n3 Voltar a opção inicial\033[0m\n")
            user_input = input("You: ")
            print("\n")
            if re.search(r"\b(sim|claro|quero|1)\b", user_input, flags=re.IGNORECASE):
                self.introduction_response()
            elif re.search(r"\b(n[ãa]o|nopes|nada|2)\b", user_input, flags=re.IGNORECASE):
                self.finalization.introduction()
            elif re.search(r"\b(voltar|3|retornar|voltando|voltar\satrás)\b", user_input, flags=re.IGNORECASE):
                self.finalization.travelAssistant.start_conversation()
