
import pytest
from classes.apuesta import Apuesta

def test_prueba():
    assert(True)

def test_constructor():
    a = Apuesta()
    assert(a.fichas == 0)

def test_repr():
    a = Apuesta()
    a.fichas = 4
    msj = a.__repr__()
    assert("Apuesta: " in msj)
    assert("fichas" in msj)
    assert("4" in msj)

def test_ponerFicha():
    a = Apuesta()
    a.ponerFicha(8)
    assert(a.fichas == 8)
    
    a = Apuesta()
    a.ponerFicha(4)
    assert(a.fichas == 4)
    a.ponerFicha(4)
    assert(a.fichas == 8)

def test_tomarFicha(): 
    a = Apuesta()
    a.fichas = 5
    a.tomarFicha()
    assert(a.fichas == 4)

def test_tomarFicha_error(): 
    with pytest.raises(ValueError):
        a = Apuesta()
        a.fichas = 5
        a.tomarFicha(6)

def test_tomarTodas():
    a = Apuesta()
    a.fichas = 5
    sacar = a.tomarTodas()
    assert(a.fichas == 0)
    assert(sacar == 5)
    a.fichas = 6
    sacar = a.tomarTodas()
    assert(a.fichas == 0)
    assert(sacar == 6)

