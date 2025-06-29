import unittest
from calculadora import soma, subtracao, multiplicacao, divisao

class TestCalculadora(unittest.TestCase):
    """
    Classe de testes unitários para as funções da calculadora.
    Utiliza o módulo unittest para verificar o comportamento das operações básicas.
    """

    def test_soma(self):
        """
        Testa a função soma com diferentes combinações de valores.
        """
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)
        self.assertEqual(soma(0, 0), 0)

    def test_subtracao(self):
        """
        Testa a função subtração com diferentes combinações de valores.
        """
        self.assertEqual(subtracao(5, 3), 2)
        self.assertEqual(subtracao(3, 5), -2)
        self.assertEqual(subtracao(0, 0), 0)

    def test_multiplicacao(self):
        """
        Testa a função multiplicação com diferentes combinações de valores.
        """
        self.assertEqual(multiplicacao(4, 3), 12)
        self.assertEqual(multiplicacao(-2, 3), -6)
        self.assertEqual(multiplicacao(0, 5), 0)

    def test_divisao(self):
        """
        Testa a função divisão com diferentes combinações de valores,
        incluindo o tratamento de divisão por zero.
        """
        self.assertEqual(divisao(10, 2), 5)
        self.assertEqual(divisao(5, -1), -5)
        self.assertEqual(divisao(0, 3), 0)
        self.assertEqual(divisao(5, 0), "Erro: divisão por zero não é permitida.")

if __name__ == '__main__':
    """
    Ponto de entrada do script de testes.
    Executa todos os métodos de teste da classe TestCalculadora.
    """
    unittest.main()