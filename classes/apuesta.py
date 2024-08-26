class Apuesta: 
    def __init__(self):
        self.cantfichas = 0
    def __repr__(self):
      return f"Apuesta: {self.cantfichas} fichas"
    def ponerFicha(self, fichas=1):
      self.cantfichas = self.cantfichas + fichas
    def tomarFicha(self, fichas=1):
      if (self.cantfichas < fichas):
            raise ValueError("El numero de fichas no puede ser negativo")
      self.cantfichas -= fichas
    def tomarTodas(self):
      self.cantfichas = 0
      return self.cantfichas
    def tieneFicha(self, fichas=1):
      if (self.cantfichas >= fichas):
        return True
      else:
        return False
    def estaVacia(self):
      if (self.cantfichas == 0):
        return True
      else:
        return False