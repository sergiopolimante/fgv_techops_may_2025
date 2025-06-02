#calculadora 

def calculate(num1, num2, operation):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Os parâmetros num1 e num2 devem ser numéricos.")

    operations = {
        '1': lambda x, y: x + y,  # Adição
        '2': lambda x, y: x - y,  # Subtração
   }
    return operations[operation](num1, num2)

def calculator():
    while True:
        print("\nBem-vindo à calculadora!")
        print("Selecione a operação desejada ou 'q' para sair:")
        print("1 - Adição (+)")
        print("2 - Subtração (-)")

        opcao = input("Digite sua opção (1/2) ou 'q' para sair: ").strip().lower()

        if opcao == 'q':
            print("Encerrando a calculadora...")
            break

        if opcao not in ['1','2']:
            print("Opção inválida!")
            continue

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: entrada inválida, digite números válidos.")
            continue

        try:
            resultado = calculate(num1, num2, opcao)
            print(f"Resultado = {resultado}")
            input("\nPressione Enter para continuar...")
        finally:
            print("Operação concluída...")

if __name__ == '__main__':
    calculator()