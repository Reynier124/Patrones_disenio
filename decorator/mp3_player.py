from auto_decorator import AutoDecorator

class Mp3Player(AutoDecorator):
    def __init__(self, vendible):
        super().__init__(vendible)

    def getDescripcion(self):
        return self.vendible.getDescripcion() , " + MP3 Player"
    
    def getPrecio(self):
        return self.vendible.getPrecio() + 250