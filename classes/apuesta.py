class Apuesta: 
    def __init__(self):
        self.fichas = 0
    def __repr__(self):
      return f"Apuesta: {self.fichas} fichas"
    def ponerFicha(self, fichas=1):
      self.fichas = self.fichas + fichas
    def tomarFicha(self, fichas=1):
      if (self.fichas < fichas):
            raise ValueError("El numero de fichas no puede ser negativo")
      self.fichas -= fichas
    def tomarTodas(self):
      nF = self.fichas
      self.fichas = 0
      return nF
    def tieneFicha(self, fichas=1):
      if (self.fichas >= fichas):
        return True
      else:
        return False
    def estaVacia(self):
      if (self.fichas == 0):
        return True
      else:
        return False
      
  