from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
import logging
from azure.core.pipeline.policies import HttpLoggingPolicy

logging.getLogger("azure.core.pipeline.policies.http_logging_policy").setLevel(logging.WARNING)

class SentimentAnalyzer:
    def __init__(self):
        load_dotenv()
        self.ai_endpoint = os.getenv("ANALYSIS_URI")
        self.ai_key = os.getenv("ANALYSIS_SUBSCRIPTION_KEY")

        self.credential = AzureKeyCredential(self.ai_key)
        self.ai_client = TextAnalyticsClient(endpoint=self.ai_endpoint, credential=self.credential)

    def analyze_sentiment(self, documents):
        try:
            sentiment_analysis = self.ai_client.analyze_sentiment(documents)
            return sentiment_analysis[0].sentiment
            
        except Exception as ex:
            print(ex)

