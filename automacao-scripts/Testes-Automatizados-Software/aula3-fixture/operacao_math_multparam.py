import pytest

def operacao(a,b,operador):
    if operador == 'soma':
        return a+b
    elif operador == 'multiplicar':
        return a*b
    elif operador == 'subtracao':
        return a-b
    elif operador == 'divisao':
        return a / b
    else:
        raise ValueError("----------operador invalido--------:/")

@pytest.mark.parametrize('a, b, operador, esperado',[
    (2, 3,'soma', 5),
    (2, 3, 'multiplicar', 6),
    (5, 3, 'subtracao', 2),
    (10, 2, 'divisao', 5),
    (10, 0, 'divisao', ZeroDivisionError) #teste com divisão por zero
])
def test_operacao(a, b, operador, esperado):
    if operador == 'divisao' and b == 0:
        #verifica se deu erro por divisão por zero
        with pytest.raises(ZeroDivisionError):
            operacao(a, b, operador)
    else:
        assert operacao(a, b, operador) == esperado