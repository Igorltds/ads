from src.medida import Medida
import pytest

@pytest.fixture
def medida():
    return Medidas(2, 3)


def test_passar_raio_devolver_valor_valido(medida):
    assert medida.get_raio()==2

def test_passar_altura_devolver_valor_valido(medida):
    assert medida.get_altura()==3

