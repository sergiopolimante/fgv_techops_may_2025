# FGV - Techops - Grupo 9

## Integrante
- Alex Medeiros
- Maiara Aguiar
- Eron Brunelli
- Antônio Cruz
- Luciana Bertochi

## Calculadora Básica em Python

Este projeto implementa uma calculadora de linha de comando em Python, trazendo as operações matemáticas básicas (adição, subtração, multiplicação e divisão), histórico de operações, tratamento robusto de erros e testes unitários com 100% de cobertura.

## Estrutura do Projeto

**Descrição dos arquivos:**

- `calculadora.py`  
  Implementa a classe Calculadora, contendo os métodos das operações matemáticas e gerenciamento do histórico.
  Interface de linha de comando que interage com o usuário, instanciando a calculadora e processando as operações.

- `test_calculadora.py`  
  Testes unitários completos, garantindo aproximadamente 100% de cobertura incluindo tratamento de erros e interface.

- `requirements.txt`  
  Lista de dependências para rodar os testes e gerar o relatório de cobertura de código.

- `README.md`  
  Este arquivo de documentação.

---

## Como executar a calculadora

1. **Clone o repositório:**

    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd <PASTA_DO_PROJETO>
    cd grupo_9
    ```

2. **(Opcional) Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    # No Linux/Mac:
    source venv/bin/activate
    # No Windows:
    venv\Scripts\activate
    ```

3. **Instale as dependências para testes/cobertura:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Execute a calculadora:**

    ```bash
    python calculadora.py
    ```

O menu será exibido no terminal. Escolha a operação, visualize o histórico, limpe o histórico ou saia conforme desejado.

---

## Como rodar os testes

- **Executar os testes unitários:**

    ```bash
    python -m unittest test_calculadora.py -v
    ```

- **Executar testes com relatório de cobertura:**

    ```bash
    coverage run --source=calculadora -m unittest test_calculadora.py
    coverage report -m
    ```

- **Gerar e visualizar o relatório HTML de cobertura:**

    ```bash
    coverage html
    # Abra o arquivo htmlcov/index.html em seu navegador.
    ```

---

## Funcionalidades

- Adição, subtração, multiplicação e divisão
- Histórico de operações
- Limpeza do histórico
- Tratamento de erros: entrada inválida, divisão por zero, erro de tipo, interrupção do usuário
- Interface no terminal
- 98% de cobertura nos testes unitários

---

## Observações

- O código segue boas práticas Python e está completamente documentado por docstrings.
- Compatível com Python 3.6 ou superior.

---
