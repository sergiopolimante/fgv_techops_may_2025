# calculadora.py

def soma(a, b):
    """
    Realiza a soma de dois números.

    Args:
        a (int/float): Primeiro número da operação
        b (int/float): Segundo número da operação

    Returns:
        int/float: O resultado da soma de a + b

    Examples:
        >>> soma(5, 3)
        8
        >>> soma(-1, 1)
        0
        >>> soma(2.5, 3.7)
        6.2
    
    Raises:
        TypeError: Se os argumentos não forem números
    """
    return a + b

# calculadora.py

# ... (mantenha a função soma e outras funções existentes) ...

def subtracao(a, b):
    """
    Realiza a subtração de dois números.

    Args:
        a (int/float): O minuendo (número do qual se subtrai)
        b (int/float): O subtraendo (número a ser subtraído)

    Returns:
        int/float: O resultado da subtração de a - b

    Examples:
        >>> subtracao(5, 3)
        2
        >>> subtracao(-1, 1)
        -2
        >>> subtracao(10.5, 3.2)
        7.3
    
    Raises:
        TypeError: Se os argumentos não forem números
    """
    return a - b

def multiplicacao(a, b):
    """
    Retorna o produto de dois números.

    Esta função realiza a multiplicação de dois números fornecidos
    como argumentos e retorna o resultado.

    Parâmetros:
    a (int ou float): O primeiro número a ser multiplicado.
    b (int ou float): O segundo número a ser multiplicado.

    Retorna:
    int ou float: O produto de a e b.

    Exemplo:
    >>> multiplicacao(3, 4)
    12
    >>> multiplicacao(2.5, 2)
    5.0
    """
    return a * b

def divisao(a, b):
    """
    Retorna o resultado da divisão de dois números.

    Esta função realiza a divisão do primeiro número pelo segundo,
    incluindo tratamento para divisão por zero.

    Parâmetros:
    a (int ou float): Numerador - número a ser dividido.
    b (int ou float): Denominador - número pelo qual será dividido.

    Retorna:
    float: O resultado da divisão de a por b.
    str: Mensagem de erro caso ocorra divisão por zero.

    Exceções:
    - Retorna mensagem de erro se o denominador for zero.

    Exemplos:
    >>> divisao(10, 2)
    5.0
    >>> divisao(7, 2)
    3.5
    >>> divisao(5, 0)
    'Erro: Divisão por zero não é permitida'
    """
    try:
        if b == 0:
            raise ZeroDivisionError
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida"


# Exemplo de uso da função
if __name__ == "__main__":
    # Testando a função
    resultado_soma = soma(5, 3)
    print(f"A soma de 5 e 3 é: {resultado_soma}")

    resultado_subtracao = subtracao(10, 4)
    print(f"A subtração de 10 e 4 é: {resultado_subtracao}")

    # Exemplo com números inteiros
    num1 = 5
    num2 = 3
    resultado1 = multiplicacao(num1, num2)
    print(f"A multiplicação de {num1} x {num2} = {resultado1}")

    # Exemplo com números decimais
    num3 = 2.5
    num4 = 4.0
    resultado2 = multiplicacao(num3, num4)
    print(f"A multiplicação de {num3} x {num4} = {resultado2}")

    # Exemplo 1: Divisão com números inteiros
    num1 = 10
    num2 = 2
    resultado1 = divisao(num1, num2)
    print(f"A divisão de {num1} ÷ {num2} = {resultado1}")

    # Exemplo 2: Divisão com número decimal
    num3 = 7.5
    num4 = 2.5
    resultado2 = divisao(num3, num4)
    print(f"A divisão de {num3} ÷ {num4} = {resultado2}")

    # Exemplo 3: Tentativa de divisão por zero
    num5 = 5
    num6 = 0
    resultado3 = divisao(num5, num6)
    print(f"A divisão de {num5} ÷ {num6} = {resultado3}")




