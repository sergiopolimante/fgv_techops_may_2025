from calculadora import soma, subtracao, multiplicacao, divisao

print("Calculadora Simples – Grupo 5")

while True:
    print("\nOperações disponíveis: soma, subtracao, multiplicacao, divisao")
    print("Digite 'sair' para encerrar.")
    op = input("Escolha a operação: ").strip().lower()

    if op == "sair" or op == "exit":
        print("Encerrando a calculadora. Até mais!")
        break

    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        if op == "soma":
            print("Resultado:", soma(a, b))
        elif op == "subtracao":
            print("Resultado:", subtracao(a, b))
        elif op == "multiplicacao":
            print("Resultado:", multiplicacao(a, b))
        elif op == "divisao":
            try:
                print("Resultado:", divisao(a, b))
            except ValueError as e:
                print("Erro:", e)
        else:
            print("Operação inválida.")
    except ValueError:
        print("Por favor, insira apenas números válidos.")

