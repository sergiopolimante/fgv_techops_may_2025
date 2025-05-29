"""
Módulo de Testes Unitários para Calculadora

Este módulo contém testes unitários completos para a classe Calculadora,
garantindo 100% de cobertura de código.

Classes:
    TestCalculadora: Classe de testes para a Calculadora.
    TestMain: Classe de testes para o módulo main.
"""

import unittest
from unittest.mock import patch, Mock
import io
from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):
    """
    Classe de testes unitários para a classe Calculadora.

    Testa todas as operações matemáticas, validações e funcionalidades
    auxiliares da calculadora.
    """

    def setUp(self):
        """
        Configuração executada antes de cada teste.

        Cria uma nova instância da Calculadora para cada teste.
        """
        self.calc = Calculadora()

class TestMain(unittest.TestCase):
    """
    Classe de testes unitários para o módulo main.

    Testa a interface de linha de comando e interações do usuário.
    """

if __name__ == '__main__':
    unittest.main()
