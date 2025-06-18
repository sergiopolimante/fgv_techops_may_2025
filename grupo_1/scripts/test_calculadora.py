{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww18540\viewh12300\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import unittest\
from calculadora import soma, subtracao, multiplicar, divisao\
\
class TestCalculadora(unittest.TestCase):\
    """\
    Classe de testes para a calculadora\
    """\
    \
    # Testes para soma (mantidos do exemplo anterior)\
    def test_soma_inteiros(self):\
        """Testa soma de dois n\'fameros inteiros positivos"""\
        self.assertEqual(soma(5, 3), 8)\
        \
    def test_soma_negativos(self):\
        """Testa soma com n\'fameros negativos"""\
        self.assertEqual(soma(-1, -1), -2)\
        self.assertEqual(soma(-1, 1), 0)\
        \
    def test_soma_floats(self):\
        """Testa soma com n\'fameros decimais"""\
        self.assertAlmostEqual(soma(2.5, 3.7), 6.2)\
        \
    def test_soma_zero(self):\
        """Testa soma com zero"""\
        self.assertEqual(soma(0, 5), 5)\
        self.assertEqual(soma(5, 0), 5)\
        self.assertEqual(soma(0, 0), 0)\
\
    # Novos testes para subtra\'e7\'e3o\
    def test_subtracao_inteiros(self):\
        """Testa subtra\'e7\'e3o de dois n\'fameros inteiros positivos"""\
        self.assertEqual(subtracao(5, 3), 2)\
        self.assertEqual(subtracao(10, 5), 5)\
        \
    def test_subtracao_negativos(self):\
        """Testa subtra\'e7\'e3o com n\'fameros negativos"""\
        self.assertEqual(subtracao(-1, -1), 0)\
        self.assertEqual(subtracao(-1, 1), -2)\
        self.assertEqual(subtracao(1, -1), 2)\
        \
    def test_subtracao_floats(self):\
        """Testa subtra\'e7\'e3o com n\'fameros decimais"""\
        self.assertAlmostEqual(subtracao(10.5, 3.2), 7.3)\
        self.assertAlmostEqual(subtracao(5.5, 2.1), 3.4)\
        \
    def test_subtracao_zero(self):\
        """Testa subtra\'e7\'e3o com zero para evitar erro"""\
        self.assertEqual(subtracao(5, 0), 5)\
        self.assertEqual(subtracao(0, 5), -5)\
        self.assertEqual(subtracao(0, 0), 0)\
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 #Insercao dos testes das fun\'e7\'f5es multiplicar e divis\'e3o:/\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0
\cf0 \
class TestMultiplicacao(unittest.TestCase):\
\
    def test_multiplicacao_positivos(self):\
        self.assertEqual(multiplicar(3, 4), 12)\
\
    def test_multiplicacao_negativos(self):\
        self.assertEqual(multiplicar(-2, -5), 10)\
\
    def test_multiplicacao_positivo_negativo(self):\
        self.assertEqual(multiplicar(6, -3), -18)\
\
    def test_multiplicacao_por_zero(self):\
        self.assertEqual(multiplicar(0, 100), 0)\
        self.assertEqual(multiplicar(100, 0), 0)\
\
    def test_multiplicacao_decimais(self):\
        self.assertAlmostEqual(multiplicar(2.5, 4), 10.0)\
        self.assertAlmostEqual(multiplicar(-1.5, 2), -3.0)\
\
def test_divisao_positivos(self):\
        self.assertEqual(divisao(10, 2), 5)\
\
    def test_divisao_negativos(self):\
        self.assertEqual(divisao(-10, -2), 5)\
\
    def test_divisao_positivo_negativo(self):\
        self.assertEqual(divisao(10, -2), -5)\
\
    def test_divisao_por_zero(self):\
        with self.assertRaises(ValueError):\
            divisao(10, 0)\
\
    def test_divisao_decimais(self):\
        self.assertAlmostEqual(divisao(5.5, 2), 2.75)\
        self.assertAlmostEqual(divisao(-7.5, 3), -2.5)\
\
    def test_divisao_resultado_inteiro(self):\
        self.assertEqual(divisao(9, 3), 3)\
        self.assertEqual(divisao(15, 5), 3)\
\
if _name_ == '_main_':\
    unittest.main()\
\
}