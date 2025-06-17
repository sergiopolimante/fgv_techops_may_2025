def multiplicacao(a: float, b: float) -> float:
    """
    Realiza a multiplicação de dois números.

    Args:
        a (float): Primeiro fator.
        b (float): Segundo fator.

    Returns:
        float: Produto de a e b.
    """
    return a * b
    
def subtracao(a: float, b: float) -> float:
    """
    Realiza a subtração de dois números.

    Args:
        a (float): Minuendo.
        b (float): Subtraendo.

    Returns:
        float: Resultado da diferença entre a e b.
    """
    return a - b


def adicao(a: float, b: float) -> float:
    """
    Realiza a adição de dois números.
    Alteração efetuada por Alex da Silva
    Args:
        a (float): Primeiro operando.
        b (float): Segundo operando.

    Returns:
        float: Resultado da soma de a e b.
    """
    return a + b

def divisao(a: float, b: float) -> float:
    """
    Realiza a divisão de dois números.
    Criado pelo Luiz Gustavo - a58495398

    Args:
        a (float): Dividendo.
        b (float): Divisor.

    Raises:
        ZeroDivisionError: Se b for zero.

    Returns:
        float: Quociente de a por b.
    """
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b

if __name__ == "__main__":
    print("5 + 2 =", adicao(5, 2))
    print("5 / 2 = ", divisao(5, 2))
    print("5 - 2 =", subtracao(5, 2))
    print("5 * 2 =", multiplicacao(5, 2))