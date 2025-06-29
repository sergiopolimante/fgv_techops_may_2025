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

    def add(self, a, b):
        """
        Realiza a adição de dois números.
        
        Args:
            a (float): Primeiro número.
            b (float): Segundo número.
            
        Returns:
            float: Resultado da adição de a + b.
            
        Raises:
            TypeError: Se a ou b não forem números.
            
        Example:
            >>> calc = Calculadora()
            >>> calc.add(5, 3)
            8
        """
        self._validate_numbers(a, b)
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        """
        Realiza a subtração de dois números.

        Args:
            a (float): Número do qual se subtrai (minuendo).
            b (float): Número a ser subtraído (subtraendo).

        Returns:
            float: Resultado da subtração de a - b.

        Raises:
            TypeError: Se a ou b não forem números.

        Example:
            >>> calc = Calculadora()
            >>> calc.subtract(10, 4)
            6
        """
        self._validate_numbers(a, b)
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
        
    def multiply(self, a, b):
        """
        Realiza a multiplicação de dois números.

        Args:
            a (float): Primeiro fator.
            b (float): Segundo fator.

        Returns:
            float: Resultado da multiplicação de a * b.

        Raises:
            TypeError: Se a ou b não forem números.

        Example:
            >>> calc = Calculadora()
            >>> calc.multiply(4, 7)
            28
        """
        self._validate_numbers(a, b)
        result = a * b
        self._add_to_history(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        """
        Realiza a divisão de dois números.
        
        Args:
            a (float): Dividendo.
            b (float): Divisor.
            
        Returns:
            float: Resultado da divisão de a / b.
            
        Raises:
            TypeError: Se a ou b não forem números.
            ValueError: Se b for zero.
            
        Example:
            >>> calc = Calculadora()
            >>> calc.divide(20, 4)
            5.0
        """
        self._validate_numbers(a, b)
        if b == 0:
            raise ValueError("Divisão por zero não é permitida")
        result = a / b
        self._add_to_history(f"{a} / {b} = {result}")
        return result

    def _validate_numbers(self, a, b):
        """
        Valida se os argumentos são números.

        Args:
            a: Primeiro valor a ser validado.
            b: Segundo valor a ser validado.

        Raises:
            TypeError: Se a ou b não forem números (int ou float) ou forem booleanos.
        """
        # Verifica se são booleanos primeiro (bool é subclasse de int)
        if isinstance(a, bool) or isinstance(b, bool):
            raise TypeError("Os argumentos devem ser números")

        # Depois verifica se são números
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Os argumentos devem ser números")

    def _add_to_history(self, operation):
        """
        Adiciona uma operação ao histórico.

        Args:
            operation (str): String representando a operação realizada.
        """
        self.history.append(operation)

    def clear_history(self):
        """
        Limpa o histórico de operações.

        Remove todas as operações armazenadas no histórico.
        """
        self.history = []

    def get_history(self):
        """
        Retorna o histórico de operações.

        Returns:
            list: Lista contendo todas as operações realizadas.
        """
        return self.history.copy()

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
