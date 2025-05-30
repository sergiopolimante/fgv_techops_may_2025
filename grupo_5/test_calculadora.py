import unittest
from calculadora import soma, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(3, 4), 7)

    def test_subtracao(self):
        self.assertEqual(subtracao(10, 4), 6)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 5), 15)

    def test_divisao(self):
        self.assertEqual(divisao(8, 2), 4)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            divisao(10, 0)

if __name__ == '__main__':
    unittest.main()
