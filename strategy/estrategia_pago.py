from abc import ABC, abstractmethod

class EstrategiaPago(ABC):
    @abstractmethod
    def pago(self, monto:float):
        pass
