from authetication.notification import EmailSender


# In case of real projects, review architecture and implement database logic (CosmosDb Azure or PostgresSql)

class Backend:
    def __init__(self, register):
        self.user_data = {}
        self.auto_increment_id = 1
        self.register = register
        self.email_sender = EmailSender()

    def register_user(self, nome, email):
        user_id = self.auto_increment_id
        self.auto_increment_id += 1  

        if user_id not in self.user_data:
            self.user_data[user_id] = {'nome': nome, 'email': email}
            print(f"Usuário {nome} registrado com sucesso! ID: {user_id}")
            self.email_sender.send_registration_email(email)
            self.login.introduction()
        else:
            print("Usuário já registrado.")
            self.register.name_input()
            
        return user_id  
    
    def get_user_data(self, email):
        return self.user_data.get(email, None)
