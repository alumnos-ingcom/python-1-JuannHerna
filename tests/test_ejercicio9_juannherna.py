###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

import pytest
from src.ejercicio9 import factores_primos

def test_factores_primos():
    factor=10
    result = factores_primos(factor)
    num1, num2 = result
    assert isinstance (result, tuple), "El resultado deberia ser una tuple"
    assert num1==2 and num2== 5, "El resultado no es el esperado, se esperaba 2 y 5"
    
    