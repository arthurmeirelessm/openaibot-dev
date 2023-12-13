from dotenv import load_dotenv
import os
import azure.cognitiveservices.speech as speech_sdk


class Speech:
    def __init__(self):
        self.subscription_key = os.environ.get("SPEECH_SUBSCRIPTION_KEY")
        self.region = os.environ.get("REGION")

    def speech_to_text(self):
        try:
            global speech_config
            load_dotenv()
            subscription_key = "008a154a276b4700887f4a759e8c0c5b"
            region = "westus2"

            speech_config = speech_sdk.SpeechConfig(subscription_key, region)
            speech_config.speech_recognition_language = "pt-BR"

            command = self.TranscribeCommand()
            print(command.lower())

        except Exception as ex:
            print(ex)

    def TranscribeCommand(self):
        command = ""

        audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
        speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
        print("Falar agora...")
        speech = speech_recognizer.recognize_once_async().get()

        if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
            command = speech.text
        else:
            print(speech.reason)
            if speech.reason == speech_sdk.ResultReason.Canceled:
                cancellation = speech.cancellation_details
                print(cancellation.reason)
                print(cancellation.error_details)

        return command
