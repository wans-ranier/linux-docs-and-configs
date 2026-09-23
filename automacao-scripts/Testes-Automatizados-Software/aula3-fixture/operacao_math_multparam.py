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

# @pytest.mark.parametrize('a, b, operador, esperado',[
#     (2, 3,'soma', 5),
#     (2, 3, 'multiplicar', 6),
#     (5, 3, 'subtracao', 2),
#     (10, 2, 'divisao', 5),
#     (10, 0, 'divisao', ZeroDivisionError) #teste com divisão por zero
# ])
@pytest.mark.parametrize('a, b, operador, esperado',[
    (5, 5, 'multiplicar', 25),
    (10, 5, 'multiplicar', 50),
    (7, -3, 'multiplicar', -21),
    (0, 8 , 'multiplicar', 0),
    (9, 4, 'multiplicar', 36),
    (10, 5, 'soma', 15),
    (20, 10, 'soma', 30),
    (7, 3, 'soma', 10),
    (6, 8 , 'soma', 14),
    (9, 4, 'soma', 13),
    (10, 5, 'subtracao', 5),
    (20, 10, 'subtracao', 10),
    (7, 3, 'subtracao', 4),
    (6, 8 , 'subtracao', -2),
    (9, 4, 'subtracao', 5)
])
def test_operacao(a, b, operador, esperado):
    if operador == 'divisao' and b == 0:
        #verifica se deu erro por divisão por zero
        with pytest.raises(ZeroDivisionError):
            operacao(a, b, operador)
    else:
        assert operacao(a, b, operador) == esperado