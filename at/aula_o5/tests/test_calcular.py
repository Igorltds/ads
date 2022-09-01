import sys
sys.path.insert(1,'/home/luaa/projects/ads/Automaçãotestes/aula_o5')

from src.calcular import Calcular
from src.medida import Medidas
import pytest

@pytest.fixture
def calculo():
    raio=Medidas(2,3)
    calculo = Calcular(raio)
    return calculo


def test_passar_valor_area_devolver_valor_raio():
    assert calculo.calcular_area() == 12.56

def test_passar_valor_area_devolver_valor_altura():
    assert calculo.calcular_volume() == 12.56


