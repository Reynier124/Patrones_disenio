from usuario import User

class ConcreteUser(User):
    def send(self, message: str):
        print(f"{self.name} envía: {message}")
        self.mediator.send_message(message, self)
    
    def receive_message(self, message:str):
        print(f"{self.name} recibe: {message}")