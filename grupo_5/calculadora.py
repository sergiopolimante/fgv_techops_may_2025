def soma(a, b):
    """
    Retorna a soma de dois números.
    """
    return a + b

def subtracao(a, b):
    """
    Retorna a subtração entre dois números.
    """
    return a - b

def multiplicacao(a, b):
    """
    Retorna a multiplicação entre dois números.
    """
    return a * b

def divisao(a, b):
    """
    Retorna a divisão entre dois números. Lança erro se b for zero.
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

