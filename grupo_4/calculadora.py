def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtracao(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicacao(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def divisao(a, b):
    """Retorna a divisão de dois números."""
    if b == 0:
        return "Erro: divisão por zero não é permitida."
    else:
        return a / b
        
def main():
    print("Calculadora Python")
    print("Operações disponíveis: +  -  *  /")
    print("Digite 'q' para sair.\n")

    while True:
        operacao = input("Digite a operação (+, -, *, /) ou 'q' para sair: ").strip()
        if operacao.lower() == "q":
            print("Encerrando a calculadora. Até logo!")
            break


        if operacao not in ["+", "-", "*", "/"]:
            print("Operação inválida. Tente novamente.\n")
            continue

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: insira apenas números válidos.\n")
            continue

    if operacao == "+":
            resultado = soma(a,b)
        elif operacao == "-":
            resultado = subtracao(a,b)
        elif operacao == "*":
            resultado = multiplicacao(a,b)
        elif operacao == "/":
            resultado = divisao(a,b)
        else:
            resultado = "Operação inválida."

        print(f"Resultado: {resultado}\n")

if __name__ == "__main__":
    main()


