class Jugador: 
    def __init__(self, nombre, fichas=5):
        self.nombre = nombre
        self.fichas = fichas
    def __repr__(self):
      return f"{self.nombre}, {self.fichas} fichas"
    def darFicha(self, cantfichas=1):
       self.fichas += cantfichas
    def sacarFicha(self, cantfichas):
       if (self.fichas < cantfichas):
            raise ValueError("La cantidad de fichas a sacar es mayor a lo que tiene el jugador.")
       self.fichas -= cantfichas
    def tieneFicha(self, fichas=1):
        if (self.fichas > fichas):
            return True
        else: 
            return False
    def sinFichas(self):
      if (self.fichas == 0):
        return True
      else:
        return False