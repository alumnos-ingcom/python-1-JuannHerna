###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############
import pytest
from src.ejercicio5 import division_lenta

def test_division_cociente():
    num1= 17
    num2= 3
    result= division_lenta(num1,num2)
    assert isinstance(result, tuple), "El resultado esperado deberia ser una tupla"
    