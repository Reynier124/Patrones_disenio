from carrito import Carrito
from pago_fisico import PagoFisico
from pago_paypal import PagoPayPal
from pago_tarjeta import PagoTarjeta

carrito = Carrito(PagoFisico())
carrito.pagar(14200)
carrito.seleccionar_metodo_pago(PagoPayPal())
carrito.pagar(150993)
carrito.seleccionar_metodo_pago(PagoTarjeta())
carrito.pagar(90340.33)

