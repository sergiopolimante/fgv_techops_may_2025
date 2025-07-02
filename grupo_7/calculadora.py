def validar_entrada(a, b):
    """
    Valida se os parâmetros fornecidos são números (int ou float).
    Lança TypeError caso contrário.
    """
    tipos_validos = (int, float)
    if not isinstance(a, tipos_validos) or not isinstance(b, tipos_validos):
        raise TypeError(f"Os parâmetros devem ser números (int ou float). Recebido: {type(a).__name__}, {type(b).__name__}")

def soma(a: float, b: float) -> float:
    """
    Retorna a soma de dois números.

    :param a: Primeiro número (int ou float)
    :param b: Segundo número (int ou float)
    :return: Resultado da soma
    """
    validar_entrada(a, b)
    return a + b

def subtracao(a: float, b: float) -> float:
    """
    Retorna a subtração entre dois números.

    :param a: Minuendo (int ou float)
    :param b: Subtraendo (int ou float)
    :return: Resultado da subtração
    """
    validar_entrada(a, b)
    return a - b

def multiplicacao(a: float, b: float) -> float:
    """
    Retorna a multiplicação entre dois números.

    :param a: Primeiro número (int ou float)
    :param b: Segundo número (int ou float)
    :return: Resultado da multiplicação
    """
    validar_entrada(a, b)
    return a * b

def divisao(a: float, b: float) -> float:
    """
    Retorna a divisão entre dois números.

    :param a: Dividendo (int ou float)
    :param b: Divisor (int ou float)
    :return: Resultado da divisão
    :raises ValueError: Se b for zero
    """
    validar_entrada(a, b)
    if b == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return a / b
