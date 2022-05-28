###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############
import pytest
from src.ejercicio2 import signo

""" Test 1 """

def test_busca_positivo():
    numero= 45
    resulta= signo(numero)
    assert isinstance(resulta, int), "el resultado debe ser un número entero"
    assert resulta == 1, "El resultado esperado de un numero positivo"
def test_busca_negativo():
    numero= -45
    result= signo(numero)
    assert isinstance(result, int), "el resultado debe ser un número entero"
    assert result == -1, "El resultado esperado de un numero negativo"
    
def test_busca_cero():
    numero= 0
    result= signo(numero)
    assert isinstance(result, int), "el resultado debe ser un número entero"
    assert result == 0, "Es el resultado esperado"