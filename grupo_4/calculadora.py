def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtracao(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicacao(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def divisao(a, b):
    """Retorna a divisão de dois números."""
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    else:
        return a / b
        
""" Código de captura das operações e operadores """

        if operacao not in ["+", "-", "*", "/"]:
            print("Operação inválida. Tente novamente.\n")
            continue

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: insira apenas números válidos.\n")
            continue