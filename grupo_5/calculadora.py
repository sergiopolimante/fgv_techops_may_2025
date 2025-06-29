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
    Realiza a multiplicacao de dois valores numericos com validacao de entrada,
    suporte a strings numericas.

    Args:
        a (int, float, str): Primeiro fator da multiplicacao.
        b (int, float, str): Segundo fator da multiplicacao.

    Returns:
        float: Resultado da multiplicacao.

    Raises:
        ValueError: Se os valores nao forem numericos ou nao puderem ser convertidos.
    """
    try:
        num1 = float(a)
        num2 = float(b)
        resultado = num1 * num2
        return resultado
    except ValueError:
        raise ValueError(f"Entradas invalidas: '{a}' e '{b}' devem ser numeros ou strings numericas.")
    except TypeError:
        raise TypeError(f"Tipos invalidos fornecidos: tipo(a)={type(a)}, tipo(b)={type(b)}")

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

