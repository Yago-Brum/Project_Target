class Exercicio2:
    def __init__(self, numero):
        self.numero = numero

    def pertence_a_fibonacci(self):
        fib1, fib2 = 0, 1
        while fib2 < self.numero:
            fib1, fib2 = fib2, fib1 + fib2
        return fib2 == self.numero

    def __str__(self):
        if self.pertence_a_fibonacci():
            return f"O número {self.numero} pertence à sequência de Fibonacci."
        else:
            return f"O número {self.numero} não pertence à sequência de Fibonacci."
