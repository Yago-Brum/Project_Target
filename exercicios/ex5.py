class Exercicio5:
    def __init__(self, entrada_string):
        self.entrada_string = entrada_string

    def inverter_string(self):
        return self.entrada_string[::-1]

    def __str__(self):
        return f"A string invertida é: {self.inverter_string()}"
