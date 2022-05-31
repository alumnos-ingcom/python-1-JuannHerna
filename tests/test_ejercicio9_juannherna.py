###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

import pytest
from src.ejercicio9 import factores_primos

def test_factores_primos():
    factor=10
    num1, num2= factores_primos(factor)
    assert isinstance (num1, int), "Se esperaba un numero entero"
    assert isinstance (num2, int), "Se esperaba un numero entero"
    assert num1==2 and num2==5, "Hola"
    
    