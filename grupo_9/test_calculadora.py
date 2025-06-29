"""
Módulo de Testes Unitários para Calculadora

Este módulo contém testes unitários completos para a classe Calculadora,
garantindo 100% de cobertura de código.

Classes:
    TestCalculadora: Classe de testes para a Calculadora.
    TestMain: Classe de testes para o módulo main.
"""

import unittest
from unittest.mock import patch
import io
from calculadora import Calculadora
from calculadora import main


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

    def test_add_positive_numbers(self):
        """Testa adição de números positivos."""
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)
        self.assertIn("5 + 3 = 8", self.calc.get_history())

    def test_add_negative_numbers(self):
        """Testa adição de números negativos."""
        result = self.calc.add(-5, -3)
        self.assertEqual(result, -8)

    def test_add_mixed_numbers(self):
        """Testa adição de números positivos e negativos."""
        result = self.calc.add(10, -4)
        self.assertEqual(result, 6)

    def test_add_floats(self):
        """Testa adição de números decimais."""
        result = self.calc.add(3.5, 2.5)
        self.assertEqual(result, 6.0)

    def test_add_invalid_type(self):
        """Testa adição com tipos inválidos."""
        with self.assertRaises(TypeError):
            self.calc.add("5", 3)
        with self.assertRaises(TypeError):
            self.calc.add(5, "3")

    def test_subtract_positive_numbers(self):
        """Testa subtração de números positivos."""
        result = self.calc.subtract(10, 4)
        self.assertEqual(result, 6)
        self.assertIn("10 - 4 = 6", self.calc.get_history())

    def test_subtract_negative_numbers(self):
        """Testa subtração de números negativos."""
        result = self.calc.subtract(-5, -3)
        self.assertEqual(result, -2)

    def test_subtract_resulting_negative(self):
        """Testa subtração resultando em número negativo."""
        result = self.calc.subtract(3, 10)
        self.assertEqual(result, -7)

    def test_subtract_floats(self):
        """Testa subtração de números decimais."""
        result = self.calc.subtract(7.5, 2.5)
        self.assertEqual(result, 5.0)

    def test_subtract_invalid_type(self):
        """Testa subtração com tipos inválidos."""
        with self.assertRaises(TypeError):
            self.calc.subtract(None, 5)
        with self.assertRaises(TypeError):
            self.calc.subtract(5, [])

    def test_multiply_positive_numbers(self):
        """Testa multiplicação de números positivos."""
        result = self.calc.multiply(4, 7)
        self.assertEqual(result, 28)
        self.assertIn("4 * 7 = 28", self.calc.get_history())

    def test_multiply_negative_numbers(self):
        """Testa multiplicação de números negativos."""
        result = self.calc.multiply(-3, -4)
        self.assertEqual(result, 12)

    def test_multiply_by_zero(self):
        """Testa multiplicação por zero."""
        result = self.calc.multiply(100, 0)
        self.assertEqual(result, 0)

    def test_multiply_floats(self):
        """Testa multiplicação de números decimais."""
        result = self.calc.multiply(2.5, 4)
        self.assertEqual(result, 10.0)

    def test_multiply_invalid_type(self):
        """Testa multiplicação com tipos inválidos."""
        with self.assertRaises(TypeError):
            self.calc.multiply({}, 5)
        with self.assertRaises(TypeError):
            self.calc.multiply(5, "abc")

    def test_divide_positive_numbers(self):
        """Testa divisão de números positivos."""
        result = self.calc.divide(20, 4)
        self.assertEqual(result, 5.0)
        self.assertIn("20 / 4 = 5.0", self.calc.get_history())

    def test_divide_negative_numbers(self):
        """Testa divisão de números negativos."""
        result = self.calc.divide(-15, -3)
        self.assertEqual(result, 5.0)

    def test_divide_floats(self):
        """Testa divisão de números decimais."""
        result = self.calc.divide(7.5, 2.5)
        self.assertEqual(result, 3.0)

    def test_divide_by_zero(self):
        """Testa divisão por zero."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Divisão por zero não é permitida")

    def test_divide_invalid_type(self):
        """Testa divisão com tipos inválidos."""
        with self.assertRaises(TypeError):
            self.calc.divide("10", 5)
        with self.assertRaises(TypeError):
            self.calc.divide(5, [1, 2, 3])

    def test_history_operations(self):
        """Testa o histórico de operações."""
        self.calc.add(5, 3)
        self.calc.subtract(10, 4)
        self.calc.multiply(2, 6)
        self.calc.divide(15, 3)

        history = self.calc.get_history()
        self.assertEqual(len(history), 4)
        self.assertEqual(history[0], "5 + 3 = 8")
        self.assertEqual(history[1], "10 - 4 = 6")
        self.assertEqual(history[2], "2 * 6 = 12")
        self.assertEqual(history[3], "15 / 3 = 5.0")

    def test_clear_history(self):
        """Testa a limpeza do histórico."""
        self.calc.add(1, 1)
        self.calc.subtract(5, 2)
        self.assertEqual(len(self.calc.get_history()), 2)

        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)

    def test_get_history_returns_copy(self):
        """Testa se get_history retorna uma cópia do histórico."""
        self.calc.add(1, 1)
        history = self.calc.get_history()
        history.append("teste")

        # O histórico original não deve ser modificado
        self.assertEqual(len(self.calc.get_history()), 1)


class TestMain(unittest.TestCase):
    """
    Classe de testes unitários para o módulo main.

    Testa a interface de linha de comando e interações do usuário.
    """

    @patch('builtins.input', side_effect=['1', '5', '3', '7'])
    def test_main_addition(self, mock_input):
        """Testa a função main com operação de adição."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("5.0 + 3.0 = 8.0", output)

    @patch('builtins.input', side_effect=['2', '10', '4', '7'])
    def test_main_subtraction(self, mock_input):
        """Testa a função main com operação de subtração."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("10.0 - 4.0 = 6.0", output)

    @patch('builtins.input', side_effect=['3', '6', '7', '7'])
    def test_main_multiplication(self, mock_input):
        """Testa a função main com operação de multiplicação."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("6.0 * 7.0 = 42.0", output)

    @patch('builtins.input', side_effect=['4', '20', '5', '7'])
    def test_main_division(self, mock_input):
        """Testa a função main com operação de divisão."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("20.0 / 5.0 = 4.0", output)

    @patch('builtins.input', side_effect=['4', '10', '0', '7'])
    def test_main_division_by_zero(self, mock_input):
        """Testa a função main com divisão por zero."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Divisão por zero não é permitida", output)

    @patch('builtins.input', side_effect=['1', 'abc', '7'])
    def test_main_invalid_number(self, mock_input):
        """Testa a função main com entrada inválida."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Erro:", output)

    @patch('builtins.input', side_effect=['5', '7'])
    def test_main_show_empty_history(self, mock_input):
        """Testa a função main mostrando histórico vazio."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Histórico vazio", output)

    @patch('builtins.input', side_effect=['1', '5', '3', '5', '7'])
    def test_main_show_history_with_operations(self, mock_input):
        """Testa a função main mostrando histórico com operações."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("HISTÓRICO DE OPERAÇÕES", output)
            self.assertIn("5.0 + 3.0 = 8.0", output)

    @patch('builtins.input', side_effect=['1', '2', '3', '6', '5', '7'])
    def test_main_clear_history(self, mock_input):
        """Testa a função main limpando o histórico."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Histórico limpo com sucesso!", output)
            self.assertIn("Histórico vazio", output)

    @patch('builtins.input', side_effect=['8', '7'])
    def test_main_invalid_option(self, mock_input):
        """Testa a função main com opção inválida."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Opção inválida", output)

    @patch('builtins.input', side_effect=KeyboardInterrupt())
    def test_main_keyboard_interrupt(self, mock_input):
        """Testa a função main com interrupção do teclado."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Operação cancelada pelo usuário", output)

    @patch('builtins.input', side_effect=['7'])
    def test_main_exit(self, mock_input):
        """Testa a função main com saída normal."""
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Encerrando calculadora", output)

    @patch('builtins.input', side_effect=['1', '5', '3', '7'])
    @patch('calculadora.Calculadora.add')
    def test_main_type_error_in_operation(self, mock_add, mock_input):
        """Testa TypeError durante operação matemática."""
        # Simula um TypeError quando add é chamado
        mock_add.side_effect = TypeError("Tipo inválido")

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Erro: Tipo inválido", output)

    @patch('builtins.input', side_effect=['2', '10', '4', '7'])
    @patch('calculadora.Calculadora.subtract')
    def test_main_type_error_in_subtract(self, mock_subtract, mock_input):
        """Testa TypeError durante subtração."""
        # Simula um TypeError quando subtract é chamado
        mock_subtract.side_effect = TypeError("Os argumentos devem ser números")

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Erro: Os argumentos devem ser números", output)

    @patch('builtins.input', side_effect=[Exception("Erro inesperado simulado"), '7'])
    def test_main_unexpected_exception(self, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Erro inesperado: Erro inesperado simulado", output)
            self.assertIn("Encerrando calculadora", output)

    @patch('builtins.input')
    def test_main_generic_exception_in_loop(self, mock_input):
        """Testa exceção genérica dentro do loop principal."""
        # Primeiro input causa uma exceção, segundo sai do programa
        mock_input.side_effect = [Exception("Erro genérico"), '7']

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("Erro inesperado: Erro genérico", output)
            self.assertIn("Encerrando calculadora", output)


if __name__ == '__main__':
    unittest.main()
