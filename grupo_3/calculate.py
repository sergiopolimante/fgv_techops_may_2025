"""
Módulo de calculadora para operações aritméticas básicas.

Uso:
    Este módulo fornece duas funções principais:
    1. `calculate(num1, num2, operation)`: executa a operação aritmética solicitada.
    2. `calculator()`: inicializa a interface de linha de comando para interação direta.

Exemplo:
    from calculate import calculate
    
    resultado = calculate(10, 2, '1')
    print(resultado)  # 12
"""

# calculadora

def calculate(num1, num2, operation):
    """
    Executa uma operação aritmética de acordo com a opção informada.

    Args:
        num1 (int | float): Primeiro valor numérico.
        num2 (int | float): Segundo valor numérico.
        operation (str): Código da operação:
            '1' -> Adição
            '2' -> Subtração
            '3' -> Multiplicação
            '4' -> Divisão

    Returns:
        float: Resultado da operação solicitada.

    Raises:
        TypeError: Se num1 ou num2 não forem numéricos.
        ZeroDivisionError: Se operação for divisão e num2 for 0.
        KeyError: Se a operação informada não estiver definida.
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Os parâmetros num1 e num2 devem ser numéricos.")

    operations = {
        '1': lambda x, y: x + y,  # Adição
        '2': lambda x, y: x - y,  # Subtração
        '3': lambda x, y: x * y,  # Multiplicação
        '4': lambda x, y: x / y,  # Divisão
    }

    return operations[operation](num1, num2)


def calculator():
    """
    Inicia a calculadora em modo de linha de comando.

    Funcionalidades:
        - Exibe um menu de opções
        - Permite realizar operações básicas
        - Encerra quando o usuário digita 'q'

    Observações:
        - Aceita apenas números válidos.
        - Para a opção de divisão, o segundo número deve ser maior que zero.
    """
    while True:
        print("\nBem-vindo à calculadora!")
        print("Selecione a operação desejada ou 'q' para sair:")
        print("1 - Adição (+)")
        print("2 - Subtração (-)")
        print("3 - Multiplicação (*)")
        print("4 - Divisão (/)")

        opcao = input("Digite sua opção (1/2/3/4) ou 'q' para sair: ").strip().lower()

        if opcao == 'q':
            print("Encerrando a calculadora...")
            break

        if opcao not in ['1', '2', '3', '4']:
            print("Opção inválida!")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: entrada inválida, digite números válidos.")
            continue

        # Verificação adicional para divisão
        if opcao == '4' and num2 <= 0:
            print("Erro: para divisão, o segundo número deve ser maior que zero.")
            continue

        try:
            resultado = calculate(num1, num2, opcao)
            print(f"Resultado = {resultado}")
            input("\nPressione Enter para continuar...")

        except ZeroDivisionError:
            print("Erro: divisão por zero!!")

        finally:
            print("Operação concluída...")

if __name__ == '__main__':
    calculator()
