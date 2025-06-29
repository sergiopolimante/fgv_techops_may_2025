import unittest
from calculadora import soma, multiplicacao, divisao, subtracao

class TestCalculadora(unittest.TestCase):
    """
    Classe de testes para a calculadora
    """
    
    def test_soma_inteiros(self):
        """Testa soma de dois números inteiros positivos"""
        self.assertEqual(soma(5, 3), 8)
        
    def test_soma_negativos(self):
        """Testa soma com números negativos"""
        self.assertEqual(soma(-1, -1), -2)
        self.assertEqual(soma(-1, 1), 0)
        
    def test_soma_floats(self):
        """Testa soma com números decimais"""
        self.assertAlmostEqual(soma(2.5, 3.7), 6.2)
        
    def test_soma_zero(self):
        """Testa soma com zero"""
        self.assertEqual(soma(0, 5), 5)
        self.assertEqual(soma(5, 0), 5)
        self.assertEqual(soma(0, 0), 0)

    def test_subtracao(self):
        """Testa a função de subtração"""
        # Teste com números inteiros positivos
        self.assertEqual(subtracao(5, 3), 2)
        
        # Teste com números negativos
        self.assertEqual(subtracao(-2, -3), 1)
        self.assertEqual(subtracao(-2, 3), -5)
        self.assertEqual(subtracao(2, -3), 5)
        
        # Teste com números decimais
        self.assertAlmostEqual(subtracao(5.5, 2.2), 3.3, places=2)
        self.assertAlmostEqual(subtracao(2.5, 1.25), 1.25, places=2)
        
        # Teste com zero
        self.assertEqual(subtracao(0, 5), -5)
        self.assertEqual(subtracao(5, 0), 5)
        self.assertEqual(subtracao(0, 0), 0)

    def test_subtracao_propriedades(self):
        """Testa propriedades matemáticas da subtração"""
        # Teste da propriedade: a - a = 0
        self.assertEqual(subtracao(5, 5), 0)
        self.assertEqual(subtracao(-3, -3), 0)
        
        # Teste da propriedade: a - 0 = a
        self.assertEqual(subtracao(5, 0), 5)
        self.assertEqual(subtracao(-5, 0), -5)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 4), 12)
        self.assertEqual(multiplicacao(-2, 5), -10)
        self.assertEqual(multiplicacao(2.5, 2), 5.0)
        self.assertEqual(multiplicacao(0, 100), 0)

    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5.0)
        self.assertEqual(divisao(7, 2), 3.5)
        self.assertEqual(divisao(-6, 3), -2.0)
        self.assertAlmostEqual(divisao(1, 3), 0.3333333, places=6)

    def test_divisao_por_zero(self):
        self.assertEqual(divisao(5, 0), "Erro: Divisão por zero não é permitida")



if __name__ == '__main__':
    unittest.main()

