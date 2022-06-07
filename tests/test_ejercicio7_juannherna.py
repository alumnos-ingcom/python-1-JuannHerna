###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

import pytest
from src.ejercicio7 import sexadecimal_a_decimal, decimal_a_sexadecimal

def test_sexadecimal_a_decimal():
    horas=3
    minutos=15
    segundos=44
    result= sexadecimal_a_decimal(horas,minutos,segundos)
    assert isinstance (result, int), "Se esperaba numero entero"
    assert result== 11744 , "El resultado, no es el esperado"
    
def test_decimal_a_sexadecimal():
    numero= 11744
    num1, num2, num3= decimal_a_sexadecimal(numero)
    assert isinstance (num1, int), "El resultado debe ser entero"
    assert isinstance (num2, int), "El resultado debe ser entero"
    assert isinstance (num3, int), "El resultado debe ser entero"
    assert num1==3 and num2==15 and num3==44, "No es el resultado esperado"