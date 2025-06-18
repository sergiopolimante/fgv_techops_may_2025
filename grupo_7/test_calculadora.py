import pytest
from calculadora import soma, subtracao, multiplicacao, divisao
 
def test_soma():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0

def test_subtracao():
    assert subtracao(5, 3) == 2
    assert subtracao(0, 4) == -4
    assert subtracao(-3, -2) == -1

def test_multiplicacao():
assert multiplicacao(2, 3) == 6
assert multiplicacao(-1, 5) == -5
assert multiplicacao(0, 99) == 0

def test_divisao():
assert divisao(10, 2) == 5
assert divisao(-9, 3) == -3
def test_divisao_por_zero():
with pytest.raises(ValueError):
divisao(10, 0)