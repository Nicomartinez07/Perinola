from classes.jugador import Jugador
from classes.ronda import Ronda
import pytest

def test_prueba():
    assert(True)

def test_constructor():
    r = Ronda()
    assert(r)

def test_agregarJugador():
    r = Ronda()
    j = Jugador("asdf")
    r.agregarJugador(j)
    assert(r.jugadores[0] == j)

def test_repr():
    r = Ronda()
    j = Jugador("asdf")
    r.agregarJugador(j)
    msj = r.__repr__()
    assert("asdf" in msj)
    assert("fichas" in msj)


def test_jugadorEnTurno():
    r = Ronda()
    j = Jugador("asdf")
    r.agregarJugador(j)
    msj = r.jugadorEnTurno()
    assert("Le " in msj)
    assert("toca" in msj)
    assert("a" in msj)

def test_sacarJugadoresSinFichas():
    r = Ronda()
    j1 = Jugador("asdf", 3)
    r.agregarJugador(j1)
    j2 = Jugador("dddf", 2)
    r.agregarJugador(j2)
    j3 = Jugador("aaaf", 1)
    r.agregarJugador(j3)
    j2.sacarFicha(2)
    r.sacarJugadoresSinFichas()
    assert(len(r.jugadores) == 2)

def test_pasarTurno1Jugador():
    r = Ronda()
    j1 = Jugador("asdf")
    r.agregarJugador(j1)
    r.pasarTurno()
    assert(len(r.jugadores) == 1)
    assert(r.jugadores[0] == j1)


def test_pasarTurno():
    r = Ronda()
    j1 = Jugador("asdf")
    r.agregarJugador(j1)
    j2 = Jugador("dddf")
    r.agregarJugador(j2)
    j3 = Jugador("aaaf")
    r.agregarJugador(j3)
    r.pasarTurno()
    assert(len(r.jugadores) == 3)
    assert(r.jugadores[0] == j2)
    assert(r.jugadores[1] == j3)
    assert(r.jugadores[2] == j1)

def test_quedaSoloUnJugador():
    r = Ronda()
    assert(r.quedaSoloUnJugador)


