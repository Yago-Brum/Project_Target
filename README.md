
# Desafio de Programação

Este repositório contém soluções para um conjunto de exercícios de programação em Python. Os exercícios abordam temas como cálculos matemáticos, manipulação de dados e uso de estruturas de dados. 

## Estrutura do Projeto

A estrutura do repositório é a seguinte:

```
desafio-programacao/
│
├── exercicios/
│   ├── ex1.py                 # Exercício 1
│   ├── ex2.py                 # Exercício 2
│   ├── ex3.py                 # Exercício 3
│   ├── ex4.py                 # Exercício 4
│   ├── ex5.py                 # Exercício 5
│   └── dados.json             # Dados JSON para o Exercício 3
│
└── app.py                     # Arquivo para rodar os exercícios
```

## Como Rodar o Projeto

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/desafio-programacao.git
    ```

2. **Navegue até a pasta do projeto:**
    ```bash
    cd desafio-programacao
    ```

3. **Execute o `app.py`:**
    ```bash
    python app.py
    ```

## Descrição dos Exercícios

### Exercício 1
Dado o trecho de código:

```
int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
```

O programa calcula a soma dos números de 1 a 13. O resultado é a soma de todos esses números.

### Exercício 2
O programa recebe um número e verifica se ele pertence à sequência de Fibonacci. A sequência de Fibonacci é gerada a partir de 0 e 1, e cada número subsequente é a soma dos dois números anteriores.

### Exercício 3
O exercício lê dados de um arquivo JSON e realiza os seguintes cálculos:
- Menor valor de faturamento ocorrido em um dia do mês;
- Maior valor de faturamento ocorrido em um dia do mês;
- Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

### Exercício 4
O programa calcula o percentual de representação de cada estado dentro do valor total de faturamento mensal de uma distribuidora. Os valores de faturamento são fornecidos em um dicionário.

### Exercício 5
Este exercício inverte os caracteres de uma string fornecida pelo usuário.

## Dependências

Não há dependências externas para esse projeto até o momento.

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções! Para isso, basta fazer um fork deste repositório, realizar as modificações desejadas e enviar um pull request.
