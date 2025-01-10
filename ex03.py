import json

# JSON de exemplo
dados = {
    "faturamento": [100, 200, 0, 300, 400, 0, 0, 500, 600, 0, 700]
}

def calcular_faturamento(dados):
    faturamento = [v for v in dados['faturamento'] if v > 0]
    menor = min(faturamento)
    maior = max(faturamento)
    media = sum(faturamento) / len(faturamento)
    dias_acima_media = len([v for v in faturamento if v > media])

    return menor, maior, dias_acima_media

menor, maior, dias_acima_media = calcular_faturamento(dados)
print(f"Menor faturamento: {menor}")
print(f"Maior faturamento: {maior}")
print(f"Dias acima da média: {dias_acima_media}")
