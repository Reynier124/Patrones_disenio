from vendible import Vendible
from abc import ABC, abstractmethod

class AutoDecorator(Vendible):
    def __init__(self, vendible):
        self.vendible = vendible

    @property
    def getVendible(self):
        return self.vendible
    
    @property
    def setVendible(self, vendible):
        self.vendible = vendible

    def getDescripcion(self):
        self.vendible.getDescripcion()
    
    def getPrecio(self):
        self.vendible.getPrecio()


    
