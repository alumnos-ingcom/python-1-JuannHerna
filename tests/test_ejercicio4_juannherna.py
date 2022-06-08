###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############
import pytest
from src.ejercicio4 import suma_lenta

def test_busca_int():
    numero=56
    num2= -4
    result= suma_lenta(numero,num2)
    if num2<0 or num1<0:
        assert result== numero+num2, "El resultado debe ser igual a la suma de los 2 numeros independiente si alun numero es positivo o negativo"
    assert isinstance(result,int), "El resultado debe ser positivo"