###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############
import pytest
from src.ejercicio6 import ordenar_menor_a_mayor, ordenar_mayor_a_menor

def test_menor_a_mayor():
    esperado=(1,2,3)
    uno, dos, tres= esperado
    result= ordenar_menor_a_mayor(uno,dos,tres)
    assert isinstance(result, tuple), "Se esperaba una tuple"
    assert result == esperado , "El result no esta ordenado"

def test_mayor_a_menor():
    esperado=(5,4,3)
    uno,dos,tres=esperado
    result= ordenar_mayor_a_menor(uno,dos,tres)
    assert isinstance(result, tuple), "Se esperaba una tuple"
    assert result == esperado , "El result no esta ordenado"