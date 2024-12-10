from mediator import Mediador

class ChatRoom(Mediador):
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)
    
    def send_message(self, message: str, user):
        for u in self.users:
            if u != user:
                u.receive_message(message)