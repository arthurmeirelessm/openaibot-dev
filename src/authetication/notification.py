import smtplib
import email.message
from dotenv import load_dotenv
import os
import secrets

load_dotenv()

class EmailSender:
    def __init__(self):
        self.sender_email = os.getenv("EMAIL_SENDER")
        self.password = os.getenv("PASSWORD_FOR_THE_EMAIL_I_SAWSENT")
        self.send_emails = os.getenv("SEND")

    def get_msg_object(self, student_email, title, corpo):
        msg = email.message.Message()
        msg["Subject"] = title
        msg["From"] = self.sender_email
        msg["To"] = student_email
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(corpo)
        return msg

    def send_email(self, msg):
        if self.send_emails:
            s = smtplib.SMTP("smtp.gmail.com: 587")
            s.starttls()
            s.login(msg["From"], self.password)
            s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
        else:
            print("Status: test environment. NOT SENT EMAILS")

    def send_registration_email(self, user_email):
        corpo_email = """
        É com grande satisfação que recebemos você na AeroQuest Navigator! Seja bem-vindo à nossa plataforma de compras de passagens aéreas internacionais.
        """
        title = "PARABÉNS! Você se cadastrou na AeroQuest Navigator ✈️🇬🇳🇬🇬🇬🇹🇬🇱🇧🇷🇧🇭🇬🇷"

        msg = self.get_msg_object(user_email, title, corpo_email)
        self.send_email(msg)
        
    
    def send_purchase_details(self, user_email):
        corpo_email = """
        Agradecemos por escolher a AeroQuest Navigator para sua próxima viagem! Estamos empolgados em tê-lo(a) a bordo e queremos garantir que sua experiência seja incrível do início ao fim.
        """
        title = "Confirmação de Compra - Detalhes da Sua Viagem"

        msg = self.get_msg_object(user_email, title, corpo_email)
        self.send_email(msg)
