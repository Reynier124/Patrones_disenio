from abc import ABC, abstractmethod

class Mediador(ABC):
    @abstractmethod
    def send_message(self, message:str, user):
        pass
