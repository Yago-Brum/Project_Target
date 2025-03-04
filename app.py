from exercicios.ex1 import Exercicio1
from exercicios.ex2 import Exercicio2
from exercicios.ex3 import Exercicio3
from exercicios.ex4 import Exercicio4
from exercicios.ex5 import Exercicio5  

def main():
    # Exercício 1 - Soma
    ex1 = Exercicio1()
    print(ex1)  # Usando o __str__ para imprimir o resultado

    # Exercício 2 - Fibonacci
    numero_fibonacci = int(input("\nDigite um número para verificar na sequência de Fibonacci: "))
    ex2 = Exercicio2(numero_fibonacci)
    print(ex2)  # Usando o __str__ para imprimir o resultado

    # Exercício 3 - Faturamento
    ex3 = Exercicio3()
    print(ex3)  # Usando o __str__ para imprimir o resultado

    # Exercício 4 - Percentual de Faturamento por Estado
    ex4 = Exercicio4()
    print(ex4)  # Usando o __str__ para imprimir o resultado

    # Exercício 5 - Inversão de String
    entrada_string = input("\nDigite uma string para inverter (Exercício 5): ")
    ex5 = Exercicio5(entrada_string)
    print(ex5)  # Usando o __str__ para imprimir o resultado

if __name__ == "__main__":
    main()
