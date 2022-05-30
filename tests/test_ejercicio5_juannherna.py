###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############
import pytest
from src.ejercicio5 import division_lenta, resto

def test_division_cociente():
    num1= 17
    num2= 3
    result= division_lenta(num1,num2)
    assert isinstance(result, int), "El numero deberia ser flotante"
    assert result >= 1, "El cociente no puede ser menor a 1" 
    
def test_busca_resto():
    num1= 17
    num2= 3
    result= resto(num1,num2)
    assert isinstance(result, int), "El resultado tiene que ser un numero entero"
    assert result>0, "El resultado debe ser mayor a 0"