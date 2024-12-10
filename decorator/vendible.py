from abc import ABC, abstractmethod

class Vendible(ABC):
    @abstractmethod
    def getDescripcion(self) -> str:
        pass
    @abstractmethod
    def getPrecio(self) -> int:
        pass