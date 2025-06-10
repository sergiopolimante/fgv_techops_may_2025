#### python
import unittest
from calculate import calculate

class TestCalculate(unittest.TestCase):
    def test_adicao(self):
        self.assertEqual(calculate(2, 3, '1'), 5)

    def test_subtracao(self):
        self.assertEqual(calculate(5, 2, '2'), 3)

    def test_multiplicacao(self):
        self.assertEqual(calculate(3, 4, '3'), 12)

    def test_divisao(self):
        self.assertAlmostEqual(calculate(10, 2, '4'), 5.0)

    def test_parametros_invalidos(self):
        with self.assertRaises(TypeError):
            calculate("abc", 2, '1')

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0, '4')

    def test_operacao_invalida(self):
        with self.assertRaises(KeyError):
            calculate(1, 1, '5')

if __name__ == '__main__':
    unittest.main()