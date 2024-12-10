from estrategia_pago import EstrategiaPago

class Carrito:
    def __init__(self, metodo_pago: EstrategiaPago):
        self._metodo_pago = metodo_pago
    
    def seleccionar_metodo_pago(self, metodo_pago: EstrategiaPago):
        self._metodo_pago = metodo_pago
    
    def pagar(self, monto:float):
        self._metodo_pago.pago(monto)