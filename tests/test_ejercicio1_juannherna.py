import pytest
from src.ejercicio1 import convertir_a_fahrrenheit
from src.ejercicio1 import convertir_a_centigrados

"""      Test 2
    Asigna variables a las funciones para determinar su validacion
    
"""
def busca_fahrrenheit():
    numero=56
    result= convertir_a_fahrrenheit(numero)
    assert isinstance(result, float), "El resultado debe ser un numero flotante"
    assert result > numero, "Cuenta salio bien"
    
def busca_centigrados():
    numero=67
    resultado= convertir_a_centigrados(numero)
    assert isinstance(result, float), "El resultado debe ser un numero flotante"
    assert result < numero, "Cuenta salio bien"