import json

class Exercicio3:
    def __init__(self):
        self.faturamento_diario = self.carregar_dados_json()

    def carregar_dados_json(self):
        try:
            with open('exercicios/dados.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Erro: arquivo não encontrado.")
            return []

    def calcular_faturamento(self):
        # Filtra os dias com faturamento (valor > 0)
        dias_com_faturamento = [dia for dia in self.faturamento_diario if dia['valor'] > 0]

        # Verifica se há dias com faturamento para evitar divisão por zero
        if not dias_com_faturamento:
            return "Não há dias com faturamento para análise."

        # Cálculo do menor valor (considerando apenas os dias com faturamento)
        menor_faturamento = min(dia['valor'] for dia in dias_com_faturamento)
        # Cálculo do maior valor (considerando todos os dias)
        maior_faturamento = max(dia['valor'] for dia in self.faturamento_diario)
        # Cálculo da média mensal (ignorando dias sem faturamento)
        media_faturamento = sum(dia['valor'] for dia in dias_com_faturamento) / len(dias_com_faturamento)
        # Contagem de dias com faturamento acima da média (considerando apenas os dias com faturamento)
        dias_acima_media = sum(1 for dia in dias_com_faturamento if dia['valor'] > media_faturamento)

        return menor_faturamento, maior_faturamento, dias_acima_media

    def __str__(self):
        resultado = self.calcular_faturamento()
        if isinstance(resultado, str):  # Caso não haja dias com faturamento
            return resultado
        
        menor_faturamento, maior_faturamento, dias_acima_media = resultado
        return (f"Menor valor de faturamento: R${menor_faturamento}\n"
                f"Maior valor de faturamento: R${maior_faturamento}\n"
                f"Número de dias acima da média mensal: {dias_acima_media}")
