from authetication.notification import EmailSender

class Backend:
    def __init__(self):
        self.user_data = {}
        self.auto_increment_id = 1
        self.email_sender = EmailSender()# Adicione uma variável para rastrear o ID autoincrementado.

    def register_user(self, nome, email):
        user_id = self.auto_increment_id
        self.auto_increment_id += 1  # Incrementa o ID para o próximo usuário.

        if user_id not in self.user_data:
            self.user_data[user_id] = {'nome': nome, 'email': email}
            print(f"Usuário {nome} registrado com sucesso! ID: {user_id}")
            self.email_sender.send_registration_email(email)
        else:
            print("Usuário já registrado.")

        return user_id  # Retorna o ID do usuário registrado.

    def get_user_data(self, user_id):
        return self.user_data.get(user_id, None)
