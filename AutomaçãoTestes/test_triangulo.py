import pytest 
from triangulo import triangulo

def test_triangulo_escaleno():
    assert triangulo(2,5,4) == "Triângulo Escaleno"

def test_triangulo_isoceles():
    assert triangulo(2,5,4) == "Triângulo Isóceles"

def test_triangulo_equilatero():
    assert triangulo(2,5,4) == "Triângulo equilátero"

def test_triangulo_nao_triangulo():
    assert triangulo(2,5,4) == "Não é Triângulo"

