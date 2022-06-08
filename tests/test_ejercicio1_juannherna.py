###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############
import pytest
from src.ejercicio1 import convertir_a_fahrrenheit
from src.ejercicio1 import convertir_a_centigrados

"""      Test 2
    Asigna variables a las funciones para determinar su validacion
    
"""
def test_busca_fahrrenheit():
    numero=56
    esperado=132.8
    result= convertir_a_fahrrenheit(numero)
    assert isinstance(result, float), "El resultado debe ser un numero flotante"
    assert result == esperado, "El resultado de la cuenta no es el esperado"
    
def test_busca_centigrados():
    numero=67
    esperado=19.44
    resultado= convertir_a_centigrados(numero)
    assert isinstance(resultado, float), "El resultado debe ser un numero flotante"
    assert resultado ==esperado, "El resultado de la cuenta no es el esperado"