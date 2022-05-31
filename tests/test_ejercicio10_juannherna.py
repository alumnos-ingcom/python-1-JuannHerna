###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

import pytest
from src.ejercicio10 import es_palindromo

def test_palindromo():
    text= "neuquen"
    result= es_palindromo(text)
    assert isinstance (result, bool), "El resultado debe ser bool"
    assert result, "Se esperaba result=True"
    