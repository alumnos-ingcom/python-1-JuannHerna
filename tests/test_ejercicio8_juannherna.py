###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############
import pytest
from src.ejercicio8 import es_primo

def test_primo():
    numero=17
    result= es_primo(numero)
    assert isinstance (result, bool), "El resultado debe ser un booleano"
    assert result, "Se esperaba True"
    