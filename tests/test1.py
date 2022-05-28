###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############
import pytest
from src.ejercicio2 import signo

""" Test 1 """

def test_busca_int():
    numero= -23
    funcion= signo(numero)
    assert isinstans (funcion, 1), "Esto esta bien"
