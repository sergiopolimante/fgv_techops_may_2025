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

def divisao(a: float, b: float) -> float:
    """
    Retorna a divisão entre dois números. Lança erro se b for zero.
    
    Args:
        a: Numerador
        b: Denominador (não pode ser zero)
    
    Raises:
        ValueError: Se o denominador for zero
    
    Returns:
        Resultado da divisão a/b
    """
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b

