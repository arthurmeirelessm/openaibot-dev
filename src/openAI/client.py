# Nome do arquivo: gpt3_example.py
import openai
from dotenv import load_dotenv
import os
from speech.client import Speech

class GPT3ChatClient:
    def __init__(self):
        load_dotenv()
        self.speech = Speech()
        api_key = os.environ.get("OPENAI_API_KEY")
        openai.api_key = api_key

    def generate_response(self, user_input):
        print(user_input)
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}]
        )
        self.speech.Synthesizer_input(resposta["choices"][0]["message"]["content"])

