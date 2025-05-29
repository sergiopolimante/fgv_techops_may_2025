"""
Módulo de Calculadora Básica

Este módulo implementa uma calculadora com operações matemáticas básicas
incluindo adição, subtração, multiplicação e divisão.

Classes:
    Calculadora: Classe principal que implementa as operações básicas.

"""


class Calculadora:
    """
    Classe que implementa uma calculadora com operações básicas.
    
    Esta classe fornece métodos para realizar operações matemáticas
    fundamentais: adição, subtração, multiplicação e divisão.
    
    Attributes:
        history (list): Lista que armazena o histórico de operações realizadas.
    
    Methods:
        add(a, b): Realiza a adição de dois números.
        subtract(a, b): Realiza a subtração de dois números.
        multiply(a, b): Realiza a multiplicação de dois números.
        divide(a, b): Realiza a divisão de dois números.
        clear_history(): Limpa o histórico de operações.
        get_history(): Retorna o histórico de operações.
    """

    def __init__(self):
        """
        Inicializa uma nova instância da calculadora.
        
        Cria uma lista vazia para armazenar o histórico de operações.
        """
        self.history = []


def main():
    """
    Função principal que executa a calculadora no modo interativo.

    Apresenta um menu de opções ao usuário e processa as operações
    escolhidas até que o usuário decida sair.
    """
    calc = Calculadora()

    while True:
        print("\n=== CALCULADORA BÁSICA ===")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Ver histórico")
        print("6. Limpar histórico")
        print("7. Sair")

        try:
            choice = input("\nEscolha uma opção (1-7): ")

            if choice == '7':
                print("Encerrando calculadora...")
                break

            if choice in ['1', '2', '3', '4']:
                try:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))

                    if choice == '1':
                        result = calc.add(num1, num2)
                        print(f"\nResultado: {num1} + {num2} = {result}")
                    elif choice == '2':
                        result = calc.subtract(num1, num2)
                        print(f"\nResultado: {num1} - {num2} = {result}")
                    elif choice == '3':
                        result = calc.multiply(num1, num2)
                        print(f"\nResultado: {num1} * {num2} = {result}")
                    elif choice == '4':
                        result = calc.divide(num1, num2)
                        print(f"\nResultado: {num1} / {num2} = {result}")

                except ValueError as e:
                    print(f"\nErro: {e}")
                except TypeError as e:
                    print(f"\nErro: {e}")

            elif choice == '5':
                history = calc.get_history()
                if history:
                    print("\n=== HISTÓRICO DE OPERAÇÕES ===")
                    for i, operation in enumerate(history, 1):
                        print(f"{i}. {operation}")
                else:
                    print("\nHistórico vazio.")

            elif choice == '6':
                calc.clear_history()
                print("\nHistórico limpo com sucesso!")

            else:
                print("\nOpção inválida! Por favor, escolha entre 1 e 7.")

        except KeyboardInterrupt:
            print("\n\nOperação cancelada pelo usuário.")
            break
        except Exception as e:
            print(f"\nErro inesperado: {e}")


if __name__ == "__main__":
    main()
