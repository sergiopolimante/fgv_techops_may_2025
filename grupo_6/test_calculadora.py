import unittest
from calculadora import adicao, subtracao, multiplicacao, divisao


class TestCalculadora(unittest.TestCase):
    """Testes unitários para as funções definidas em calculadora.py"""

    def test_adicao(self):
        self.assertEqual(adicao(5, 2), 7)
        self.assertAlmostEqual(adicao(-1.5, 3.2), 1.7)

    def test_subtracao(self):
        self.assertEqual(subtracao(5, 2), 3)
        self.assertAlmostEqual(subtracao(2.5, 4.1), -1.6)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(5, 2), 10)
        self.assertAlmostEqual(multiplicacao(-1.5, 2), -3.0)

    def test_divisao(self):
        self.assertEqual(divisao(6, 3), 2)
        self.assertAlmostEqual(divisao(7.5, 2.5), 3.0)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divisao(5, 0)


if __name__ == '__main__':
    unittest.main()