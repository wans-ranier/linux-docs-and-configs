import pytest
#AULA 3
#decorator para pular o teste, ou seja, ele não vai ser executado
@pytest.mark.skip(reason="este teste será ignorado temporareamente")
def test_ignorado():
    assert 1 == 1