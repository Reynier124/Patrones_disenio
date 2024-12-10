from estrategia_pago import EstrategiaPago

class PagoTarjeta(EstrategiaPago):
    def pago(self, monto):
        print(f"Pagando {monto} con tarjeta de credito")