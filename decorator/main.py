from fiat_uno import FiatUno
from mp3_player import Mp3Player
from gasoil import Gasoil
from aire_condicionado import AireAcondicionado
from ford_fiesta import FordFiesta

auto = Mp3Player(FiatUno())
auto = Gasoil(auto)

print(auto.getDescripcion())
print(f"Su precio es: {auto.getPrecio()}")

auto2 = FordFiesta()
auto2 = Mp3Player(auto2)
auto2 = Gasoil(auto2)
auto2 = AireAcondicionado(auto2)

print(auto2.getDescripcion())
print(f"Su precio es: {auto2.getPrecio()}")