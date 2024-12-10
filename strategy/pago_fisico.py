from estrategia_pago import EstrategiaPago

class PagoFisico(EstrategiaPago):
    def pago(self, monto):
        print(f"Pagando {monto} en el local")
