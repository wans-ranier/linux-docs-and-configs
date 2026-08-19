import pytest

#definindo um fixture

@pytest.fixture
def lista_numeros():
    return [1, 2, 3, 4, 5]

def test_soma(lista_numeros):
    #usar a fixture comoo argumento
    assert sum(lista_numeros) == 15

def test_max(lista_numeros):
    assert max(lista_numeros) == 5