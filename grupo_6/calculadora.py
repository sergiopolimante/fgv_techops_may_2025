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

def exibir_menu() -> None:
    """
    Exibe o menu de operações para o usuário.
    """
    print("\n=== Calculadora de Terminal ===")
    print("1. Adição (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Sair")


def obter_numero(prompt: str) -> float:
    """
    Solicita ao usuário um número float, validando a entrada.

    Args:
        prompt (str): Mensagem a ser exibida ao solicitar o número.

    Returns:
        float: Número digitado pelo usuário.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Informe um número válido.")


def main() -> None:
    """
    Função principal que controla o fluxo da calculadora.
    """
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1/2/3/4/5): ")

        if escolha == '5':
            print("Encerrando a calculadora. Até a próxima!")
            break

        if escolha not in {'1', '2', '3', '4'}:
            print("Opção inválida. Tente novamente.")
            continue

        # Obtém os operandos
        a = obter_numero("Digite o primeiro número: ")
        b = obter_numero("Digite o segundo número: ")

        try:
            if escolha == '1':
                resultado = adicao(a, b)
                simbolo = '+'  
            elif escolha == '2':
                resultado = subtracao(a, b)
                simbolo = '-'  
            elif escolha == '3':
                resultado = multiplicacao(a, b)
                simbolo = '*'  
            else:  # escolha == '4'
                resultado = divisao(a, b)
                simbolo = '/'

            print(f"\n{a} {simbolo} {b} = {resultado}\n")
        except Exception as e:
            print(f"Erro ao executar a operação: {e}")


if __name__ == "__main__":
    main()
