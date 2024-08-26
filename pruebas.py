from classes.jugador import Jugador
from classes.apuesta import Apuesta

#Jugador ----------------------------------------
"""
j = Jugador("Juan")
j2 = Jugador("maria", 10)

print(j)
print(j2)
j.darFicha(2)
print(j)

j.sacarFicha(2)
print(j)

esVerda = j.sinFichas()
print(esVerda)
"""

#Apuestas----------------------------------------

a = Apuesta()

a.ponerFicha(76)
a.tomarFicha(76)

a.ponerFicha(75)
print(a)

a.tomarTodas()
print(a)

a.ponerFicha(6)
resultado = a.estaVacia()
print(resultado)
