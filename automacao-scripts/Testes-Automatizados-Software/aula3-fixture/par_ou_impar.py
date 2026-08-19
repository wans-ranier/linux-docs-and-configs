import pytest

def eh_par(numero):
    return numero % 2 == 0

@pytest.mark.parametrize("entrada, esperado", [
    (2, True), #teste com número par
    (3, False), #teste com número ímpar
    (0, True), #teste com zero
    (-8, True), #teste com número negativo par
    (-27, False) #teste com número negativo ímpar
])
def test_eh_par(entrada, esperado):
    #executa o teste com as entradas parametrizadas
    assert eh_par(entrada) == esperado
