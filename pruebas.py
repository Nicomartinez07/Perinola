from classes.jugador import Jugador


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