import os
from dotenv import load_dotenv
import requests
import logging

load_dotenv()


class LUIS:
    def __init__(self):
        self.subscription_key = os.environ.get("SUBSCRIPTION_KEY")
        self.request_id = os.environ.get("REQUEST_ID")
        self.participant_id = os.environ.get("PARTICIPANT_ID")
        self.language_code = os.environ.get("LANGUAGE_CODE")
        self.url = os.environ.get("URL")

        self.headers = {
            "Ocp-Apim-Subscription-Key": self.subscription_key,
            "Apim-Request-Id": self.request_id,
            "Content-Type": "application/json",
        }

        self.parameters = {
            "projectName": "openaibotV3",
            "verbose": True,
            "deploymentName": "V5deploy",
            "stringIndexType": "TextElement_V8",
        }

        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def analyze_language(self, text):
        try:
            data = {
                "kind": "Conversation",
                "analysisInput": {
                    "conversationItem": {
                        "id": self.participant_id,
                        "text": text,
                        "modality": "text",
                        "language": self.language_code,
                        "participantId": self.participant_id,
                    }
                },
                "parameters": self.parameters,
            }

            response = requests.post(self.url, headers=self.headers, json=data)

            if response.status_code == 200:
                result_json = response.json()
                top_intent = (
                    result_json.get("result", {}).get("prediction", {}).get("topIntent")
                )
                entities = result_json.get("result", {}).get("prediction", {}).get("entities", [])
                
                # Pegar o primeiro item único de categories como string
                unique_category = next(iter(set([entity.get("category") for entity in entities])), None)
                
                response_json = {
                    "topIntent": top_intent,
                    "categories": unique_category
                }
                return response_json
            else:
                self.logger.error(f"Falha: {response.status_code}")
                self.logger.error(response.json())
                return None

        except requests.RequestException as e:
            self.logger.error(f"Falha na requisição: {e}")
            return None
        except Exception as ex:
            self.logger.error(f"Erro inesperado: {ex}")
            return None
        