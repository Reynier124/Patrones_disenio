from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name: str, mediator):
        self.name = name
        self.mediator = mediator
    
    @abstractmethod
    def send(self, message: str):
        pass

    @abstractmethod
    def receive_message(self, message: str):
        pass
        
