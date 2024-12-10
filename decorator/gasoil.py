from auto_decorator import AutoDecorator

class Gasoil(AutoDecorator):
    def __init__(self, vendible):
        super().__init__(vendible)
    
    def getDescripcion(self):
        return self.vendible.getDescripcion() , " + Gasoil"
    
    def getPrecio(self):
        return self.vendible.getPrecio() + 1200
    
