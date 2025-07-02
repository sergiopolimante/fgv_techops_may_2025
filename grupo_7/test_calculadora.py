import unittest
from calculadora import soma, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):

    # Testes para soma
    def test_soma_valores_positivos(self):
        self.assertEqual(soma(2, 3), 5)

    def test_soma_com_zero(self):
        self.assertEqual(soma(0, 10), 10)

    def test_soma_valores_negativos(self):
        self.assertEqual(soma(-2, -4), -6)

    def test_soma_valores_mistos(self):
        self.assertEqual(soma(-3, 7), 4)

    # Testes para subtração
    def test_subtracao_valores_positivos(self):
        self.assertEqual(subtracao(5, 2), 3)

    def test_subtracao_resultado_negativo(self):
        self.assertEqual(subtracao(2, 5), -3)

    def test_subtracao_com_zero(self):
        self.assertEqual(subtracao(0, 5), -5)

    # Testes para multiplicação
    def test_multiplicacao_basica(self):
        self.assertEqual(multiplicacao(3, 4), 12)

    def test_multiplicacao_por_zero(self):
        self.assertEqual(multiplicacao(0, 99), 0)

    def test_multiplicacao_com_negativos(self):
        self.assertEqual(multiplicacao(-2, 5), -10)
        self.assertEqual(multiplicacao(-3, -3), 9)

    # Testes para divisão
    def test_divisao_comum(self):
        self.assertEqual(divisao(10, 2), 5)

    def test_divisao_resultado_negativo(self):
        self.assertEqual(divisao(-9, 3), -3)

    def test_divisao_float(self):
        self.assertAlmostEqual(divisao(7, 2), 3.5)

    def test_divisao_por_um(self):
        self.assertEqual(divisao(5, 1), 5)

    def test_divisao_por_si_mesmo(self):
        self.assertEqual(divisao(4, 4), 1)

    def test_divisao_por_zero(self):
        with self.assertRaises(ValueError):
            divisao(10, 0)

    # Testes com entradas inválidas
    def test_soma_com_string(self):
        with self.assertRaises(TypeError):
            soma("a", 3)

    def test_multiplicacao_com_lista(self):
        with self.assertRaises(TypeError):
            multiplicacao([1, 2], 3)

    def test_divisao_com_none(self):
        with self.assertRaises(TypeError):
            divisao(None, 2)

if __name__ == '__main__':
    unittest.main()
