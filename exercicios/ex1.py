class Exercicio1:
    def __init__(self):
        self.indice = 13
        self.soma = 0
        self.k = 0

    def calcular_soma(self):
        while self.k < self.indice:
            self.k += 1
            self.soma += self.k
        return self.soma

    def __str__(self):
        return f"O valor da soma é: {self.calcular_soma()}"
