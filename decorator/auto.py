from abc import ABC, abstractmethod
from vendible import Vendible

class Auto(Vendible):
    def __init__(self):
        self.nombre = ""