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
    print("5 / 2 = ", divisao(5, 2))