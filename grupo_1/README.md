# Calculadora em Python

Este projeto implementa uma calculadora simples em Python com operações básicas de aritmética.

## Equipe
*Este projeto foi desenvolvido por:*

Alexandre Moreno  
Cassio Araujo   
Diogue Guedes  
Fabricio Quiles  
Rodrigo Sampaio  

*Contribuições*

Contribuições são bem-vindas! Por favor, sinta-se à vontade para submeter um Pull Request.

## Funcionalidades

A calculadora inclui as seguintes operações:

1. *Soma*: Adiciona dois números.
2. *Subtração*: Subtrai o segundo número do primeiro.
3. *Multiplicação*: Multiplica dois números.
4. *Divisão*: Divide o primeiro número pelo segundo, com tratamento para divisão por zero.

## Implementação

As funções implementadas são:

- soma(a, b): Retorna a soma de dois números.
- subtracao(a, b): Retorna a subtração de dois números.
- multiplicacao(a, b): Retorna a multiplicação de dois números.
- divisao(a, b): Retorna a divisão de dois números, tratando a divisão por zero.

## Como usar

Para usar a calculadora, importe as funções do arquivo calculadora.py:

```python
from calculadora import soma, subtracao, multiplicacao, divisao

# Exemplos de uso
print(soma(5, 3))        # Saída: 8
print(subtracao(10, 4))  # Saída: 6
print(multiplicacao(2, 6))  # Saída: 12
print(divisao(15, 3))    # Saída: 5.0
```

## Testes

O projeto inclui testes unitários implementados usando o framework unittest do Python. Os testes estão no arquivo test_calculadora.py.

Para executar os testes, use o comando:

    
python -m unittest test_calculadora.py


