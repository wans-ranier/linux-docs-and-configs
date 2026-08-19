import pytest
from soma import*

#pip install pytest
# não esqueça de ativar o ambiente virtual antes 
# de executar os testes -> source venv/bin/activate

#execute com pytest -v test_soma.py
# execute com pytest -v test_soma.py -k test_soma
# que significa que o pytest vai executar apenas os testes que contenham a palavra test_soma no nome do teste


#aqui estamos usando o pytest.mark.parametrize para passar diferentes valores de entrada e saída esperada para o teste test_soma
@pytest.mark.parametrize("a, b,esperado", [(1,2,3), (1,5,9),(3,4,7),(10, 20, 30)]) 

# def test_soma():
#     assert soma(2,2) == 4

#isso é um teste parametrizado, ou seja, ele vai executar o mesmo teste com diferentes valores de entrada e saída esperada
def test_soma(a,b, esperado):
    assert soma(a,b) == esperado


