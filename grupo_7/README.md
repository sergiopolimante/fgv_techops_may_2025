# 🧮 Calculadora em Python

Este projeto implementa uma calculadora simples que realiza as quatro operações básicas: soma, subtração, multiplicação e divisão. O código inclui validações robustas para garantir entradas corretas e testes automatizados abrangentes para assegurar sua funcionalidade.

---

## 📁 Estrutura do Projeto

```
calculadora/
├── calculadora.py          # Implementação das operações matemáticas
├── test_calculadora.py     # Testes automatizados com unittest
├── README.md               # Documentação detalhada do projeto
```

---

## ⚙️ Funcionalidades

Todas as funções aceitam apenas números (`int` ou `float`). Entradas inválidas geram exceções apropriadas.

| Função                | Descrição                           | Erros tratados                            |
| --------------------- | ----------------------------------- | ----------------------------------------- |
| `soma(a, b)`          | Retorna a soma entre `a` e `b`      | `TypeError` se entradas não forem números |
| `subtracao(a, b)`     | Retorna a diferença entre `a` e `b` | `TypeError` se entradas não forem números |
| `multiplicacao(a, b)` | Retorna o produto entre `a` e `b`   | `TypeError` se entradas não forem números |
| `divisao(a, b)`       | Retorna o quociente de `a` por `b`  | `TypeError`, `ValueError` (se b for zero) |

---

## 🚀 Como executar

### ▶️ Pré-requisitos

* Python 3.8 ou superior
* Git (opcional, para clonar o projeto)

### ▶️ Clonar o repositório

```bash
git clone https://github.com/usuario/projeto-calculadora.git
cd projeto-calculadora
```

### ▶️ Utilizando as funções no Python

```python
from calculadora import soma, subtracao, multiplicacao, divisao

print(soma(5, 3))              # Resultado: 8
print(subtracao(10, 4))        # Resultado: 6
print(multiplicacao(3, 7))     # Resultado: 21
print(divisao(10, 2))          # Resultado: 5.0
```

---

## ✅ Executando os testes

Os testes são realizados com o módulo `unittest`:

```bash
python -m unittest test_calculadora.py
```

O resultado esperado é algo similar a:

```
...................
----------------------------------------------------------------------
Ran 19 tests in 0.003s

OK
```

Os testes cobrem:

* Operações com números inteiros e decimais.
* Entradas negativas, zero e exceções esperadas.
* Validação contra entradas inválidas (strings, listas, None).

---

## 👥 Integrantes do Grupo
**Grupo 7**
* Ana Clara Pelaes
* Bruno Muniz
* João Ribeiro
* Leandro Fernandes
* Lucas Albuquerque 

---

## 🎓 Informações Acadêmicas

* **Disciplina:** Gestão de TechOps: DevOps, DataOps e MLOps
* **Curso:** MBA em Transformação Digital
* **Instituição:** FGV - Fundação Getúlio Vargas