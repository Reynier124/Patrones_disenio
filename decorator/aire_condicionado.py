from auto_decorator import AutoDecorator

class AireAcondicionado(AutoDecorator):
    def __init__(self, vendible):
        super().__init__(vendible)
    
    def getDescripcion(self):
        return self.vendible.getDescripcion() , " + Aire Acondicionado"

    def getPrecio(self):
        return self.vendible.getPrecio() + 1500