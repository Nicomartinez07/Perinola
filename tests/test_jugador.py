from classes.jugador import Jugador
import pytest


def test_prueba():
    assert(True)

def test_constructor():
    j = Jugador()
    j.fichas = 5
    assert(j.fichas == 5)

def test_repr():
    j = Jugador()
    j.fichas = 4
    msj = j.__repr__()
    assert("4" in msj)
    assert("fichas" in msj)

def test_darFicha():
    j = Jugador()
    j.darFicha(8)
    assert(j.fichas == 8)
    
    j = Jugador()
    j.darFicha(4)
    assert(j.fichas == 4)
    j.darFicha(4)
    assert(j.fichas == 8)

def test_sacarFicha(): 
    j = Jugador()
    j.fichas = 5
    j.sacarFicha(5)
    assert(j.fichas == 0)

def test_sacarFicha_error(): 
    with pytest.raises(ValueError):
        j = Jugador()
        j.fichas = 5
        j.sacarFicha(6)

def test_tieneFicha():
    with pytest.raises(ValueError):
        j = Jugador()
        j.fichas = 5
        j.tieneFicha(6)

def test_sinFichas():
    j = Jugador()
    j.fichas = 5
    assert(j.sinFichas)

