from estrategia_pago import EstrategiaPago

class PagoPayPal(EstrategiaPago):
    def pago(self, monto):
        print(f"Pagando {monto} con PayPal")