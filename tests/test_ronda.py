from classes.ronda import Ronda
import pytest

def test_prueba():
    assert(True)

def test_constructor():
    r = Ronda()
    assert(r)

def test_jugadorEnTurno():
    r = Ronda()
    msj = r.jugadorEnTurno()
    assert("Le: " in msj)
    assert("toca" in msj)
    assert("a" in msj)




