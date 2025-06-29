# Calculadora Simples – Grupo 5

## Descrição

Este projeto é uma calculadora simples desenvolvida em Python, capaz de realizar as quatro operações básicas: soma, subtração, multiplicação e divisão (com tratamento de erro para divisão por zero). Agora, também é possível utilizar a calculadora de modo interativo via terminal, permitindo que o usuário escolha a operação e insira os números quantas vezes quiser.

## Como usar

Você pode utilizar a calculadora de duas formas:

### 1. Modo Interativo

Execute no terminal (Anaconda Prompt), dentro da pasta do projeto:

```bash
python input.py
```

O programa exibirá as opções e pedirá para digitar a operação e os números. Para encerrar, digite `sair` na escolha da operação.

**Exemplo de uso:**

```
Calculadora Simples – Grupo 5
Operações disponíveis: soma, subtracao, multiplicacao, divisao
Escolha a operação: soma
Digite o primeiro número: 8
Digite o segundo número: 2
Resultado: 10.0
```

### 2. Modo Importação

Você pode importar as funções diretamente em outro código Python:

```python
from calculadora import soma, subtracao, multiplicacao, divisao

print(soma(2, 3))        # 5
print(subtracao(5, 2))   # 3
print(multiplicacao(4, 6)) # 24
print(divisao(10, 2))    # 5
```

## Como rodar os testes

Para garantir que todas as funções estão funcionando corretamente, execute um dos comandos abaixo no terminal, dentro da pasta do projeto:

```bash
python -m unittest test_calculadora.py
```

ou

```bash
py -m unittest test_calculadora.py
```

## Integrantes do grupo 5

* Alexandre Augusto Lima
* Bruna Texeira
* Danilo Reis
* Renato Azevedo
* Vitor Lima