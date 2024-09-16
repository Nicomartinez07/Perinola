from classes.perinola import Perinola
import pytest

def test_prueba():
    assert(True)

def test_constructor():
    p = Perinola()
    assert(p)

def test_repr():
    p = Perinola()
    msj = p.__repr__()
    assert("Salio:" in msj)
    assert("Pon 1" in msj)

def test_tirar():
    p = Perinola()
    p = p.tirar()
    mensajes = ("Pon 1", "Toma 2", "Todos Ponen",
      "Toma 1", "Pon 2", "Toma Todo")
    assert(p in mensajes)

