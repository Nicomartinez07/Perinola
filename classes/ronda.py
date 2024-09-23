class Ronda: 
    def __init__(self):
        self.jugadores = []
    
    def __repr__(self):
        return "\n".join(map(str, self.jugadores))

    def agregarJugador(self, jugador):
        if jugador.fichas <= 0:
            raise ValueError("No se puede agregar un jugador sin fichas.")
        self.jugadores.append(jugador)
    
    def sacarJugadoresSinFichas(self):
        a_sacar = []
        for i in range(0, len(self.jugadores)):
            if self.jugadores[i].sinFichas():
                a_sacar.append(i)
        for i in reversed(a_sacar):
            n = self.jugadores.pop(i)
            print(f"Perdió {n}")


    def jugadorEnTurno(self):
        return self.jugadores[0]

    def pasarTurno(self):
        j = self.jugadores.pop(0)
        self.jugadores.append(j)

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1 
        
