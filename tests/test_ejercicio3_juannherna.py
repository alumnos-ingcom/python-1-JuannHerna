###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

import pytest
from src.ejercicio3 import compara

"""
Retornar -1 si el primero es menor que el segundo
Retornar 0 si son iguales
Retornar 1 si el primero es mayor que el segundo
"""
def primero_menor():
    num1=4
    num2=6
    resulta1 = comprar(num1,num2)
    assert isinstance(resulta1, int), "El resultado debe ser entero"
    assert resulta1 == -1, "El primer numero no es el menor"

def busca_iguales():
    num1=4
    num2=4
    resulta2 = comprar(num1,num2)
    assert isinstance(resulta2, int), "El resultado tiene que ser un entero"
    assert resulta2==2, "Los numero no son iguales"
    
def primero_mayor():
    num1=8
    num2=4
    resulta3 = comprar(num1,num2)
    assert isinstance(resulta3, int), "El resultado tiene que ser entero"
    assert resulta3 == 1, "El primer numero no es el mayor"
    