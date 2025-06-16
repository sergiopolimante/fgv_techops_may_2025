# Calculadora em Python

## Integrantes
- **Nome - Matricula - Usuários GitHub**
- LUIZ GUSTAVO MARINHO DE ALMEIDA - A58495398 - LuizGustavoMarinhoDeAlmeida e Nareez
- LEONARDO BAUMEISTER DA SILVA - A58496079 - leonardobaumeister
- ALEX DA SILVA - A58497210 - Matrix0147
- KAIO ALBERTO AIRES SOUSA - A58501055 - kaioalberto e suporteplanejati
- GEOVANA VEDAN - A58511481 - GeovanaVedan

## Objetivo

Este projeto tem como objetivo de implementar uma **calculadora simples** que realiza as quatro operações básicas: soma, subtração, multiplicação e divisão. 
Acompanhada de **testes unitários** que garantem a correção e robustez de cada função.

## Funcionalidades

- `adicao(a: float, b: float) -> float`  
  Retorna a soma de `a` e `b`.

- `subtracao(a: float, b: float) -> float`  
  Retorna a diferença entre `a` e `b`.

- `multiplicacao(a: float, b: float) -> float`  
  Retorna o produto de `a` e `b`.

- `divisao(a: float, b: float) -> float`  
  Retorna o quociente de `a` por `b`.  
  Lança `ZeroDivisionError` se `b` for zero.

## Estrutura do Projeto

- **calculadora.py**: Contém a implementação da calculadora.
- **test_calculadora.py**: Contém os testes unitários da calculadora.

## Uso

   ```bash
   git clone https://github.com/LuizGustavoMarinhoDeAlmeida/fgv_techops_may_2025.git
   cd calculadora
   python calculadora.py
   python test_calculadora.py