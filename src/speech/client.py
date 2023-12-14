from dotenv import load_dotenv
import os
import azure.cognitiveservices.speech as speech_sdk

load_dotenv()

class Speech:
    def __init__(self):
        self.subscription_key = os.environ.get("SPEECH_SUBSCRIPTION_KEY")
        self.region = os.environ.get("REGION")
        self.speech_config = speech_sdk.SpeechConfig(self.subscription_key, self.region)
        self.speech_config.speech_recognition_language = "pt-BR"
        self.audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
        
    
    def TranscribeCommand(self):
        command = ""
        
        audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
        speech_recognizer = speech_sdk.SpeechRecognizer(self.speech_config, audio_config)
        print("Falar agora...")
        speech = speech_recognizer.recognize_once_async().get()
        if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
            command = speech.text
        elif speech.reason == speech_sdk.ResultReason.Canceled:
            command = None
        return command

    
    def Synthesizer_input(self, gpt_response):
        self.speech_config.speech_synthesis_voice_name = "pt-BR-YaraNeural"
        speech_synthesizer = speech_sdk.SpeechSynthesizer(self.speech_config)  
        
        speak = speech_synthesizer.speak_text_async(gpt_response).get()
        if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
            print(speak.reason)

