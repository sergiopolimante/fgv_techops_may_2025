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