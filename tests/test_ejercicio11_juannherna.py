###############
# Juan cruz Hernandez- JuannHerna
# UNRN Andina - Introducción a la Ingenieria en Computación
###############

import pytest
from src.ejercicio11 import es_multiplo


def test_multiplo():
    num=10
    multiplo=2
    result= es_multiplo(num, multiplo)
    assert isinstance (result, bool), "Resultado esperado tiene que ser booleano"
    assert result, "Se esperaba result= True"