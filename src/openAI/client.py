import openai


class GPT3ChatClient:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}]
        )
        return response["choices"][0]["message"]["content"]
