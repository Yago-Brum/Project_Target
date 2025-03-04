class Exercicio4:
    def __init__(self):
        # Definindo diretamente o dicionário com os dados de faturamento
        self.faturamento_estados = {
            "SP": 67836.43,
            "RJ": 36678.66,
            "MG": 29229.88,
            "ES": 27165.48,
            "Outros": 19849.53
        }

    def calcular_percentual(self):
        faturamento_total = sum(self.faturamento_estados.values())
        percentuais = {}

        for estado, valor in self.faturamento_estados.items():
            percentual = (valor / faturamento_total) * 100
            percentuais[estado] = round(percentual, 2)

        return percentuais

    def __str__(self):
        percentuais = self.calcular_percentual()
        resultado = "Percentual de representação de cada estado no faturamento mensal:\n"
        for estado, percentual in percentuais.items():
            resultado += f"{estado}: {percentual}%\n"
        return resultado
