#### python
import unittest
import logging
from calculate import calculate

# Ajuste de formatação para os logs
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'  # Remove informações de módulo e linha
)
logger = logging.getLogger(__name__)

class TestCalculate(unittest.TestCase):
    def setUp(self):
        logger.info("\n========================================")
        logger.info(" Iniciando novo teste")
        logger.info("========================================")

    def test_adicao(self):
        logger.info("[TESTE ADIÇÃO]\nEntrada: (2, 3, '1')")
        result = calculate(2, 3, '1')
        logger.info(f"Resultado: {result}")
        self.assertEqual(result, 5)

    def test_subtracao(self):
        logger.info("[TESTE SUBTRAÇÃO]\nEntrada: (5, 2, '2')")
        result = calculate(5, 2, '2')
        logger.info(f"Resultado: {result}")
        self.assertEqual(result, 3)

    def test_multiplicacao(self):
        logger.info("[TESTE MULTIPLICAÇÃO]\nEntrada: (3, 4, '3')")
        result = calculate(3, 4, '3')
        logger.info(f"Resultado: {result}")
        self.assertEqual(result, 12)

    def test_divisao(self):
        logger.info("[TESTE DIVISÃO]\nEntrada: (10, 2, '4')")
        result = calculate(10, 2, '4')
        logger.info(f"Resultado: {result}")
        self.assertAlmostEqual(result, 5.0)

    def test_parametros_invalidos(self):
        logger.info("[TESTE PARÂMETROS INVÁLIDOS]\nEsperando TypeError")
        with self.assertRaises(TypeError):
            calculate("abc", 2, '1')

    def test_divisao_por_zero(self):
        logger.info("[TESTE DIVISÃO POR ZERO]\nEsperando ZeroDivisionError")
        with self.assertRaises(ZeroDivisionError):
            calculate(10, 0, '4')

    def test_operacao_invalida(self):
        logger.info("[TESTE OPERAÇÃO INVÁLIDA]\nEsperando KeyError")
        with self.assertRaises(KeyError):
            calculate(1, 1, '5')

if __name__ == '__main__':
    unittest.main(verbosity=2)