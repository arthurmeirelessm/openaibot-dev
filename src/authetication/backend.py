# authetication/backend.py
from authetication.notification import EmailSender

class Backend:
    user_data = {}
    auto_increment_id = 1

    def __init__(self):
        self.email_sender = EmailSender()
        

    def register_user(self, nome, email):
        from bots.login import Login
        from bots.register import Register

        login = Login(self)
        register = Register(self)

        user_id = Backend.auto_increment_id
        Backend.auto_increment_id += 1  

        if user_id not in Backend.user_data:
            Backend.user_data[user_id] = {'nome': nome, 'email': email}
            print("Cadastro feito com sucesso! ✅\nVou redirecionar você para a seção de login.")
            #self.email_sender.send_registration_email(email)
            login.introduction()
            return login  # Retorne a instância de Login
        else:
            print("Usuário já registrado.")
            register.name_input()

    @classmethod
    def get_user_data(cls, email):
        user_data_match = {user_id: data for user_id, data in cls.user_data.items() if data['email'] == email}
        
        if user_data_match:
            print(user_data_match)
            return True
        else:
            False

