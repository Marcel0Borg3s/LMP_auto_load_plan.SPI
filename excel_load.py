import os
from openpyxl import load_workbook

def carregar_codigos_excel(planilha_caminho, abas_alvo=['2025', '2024']):
    # 1. Abrir a planilha
    wb = load_workbook(planilha_caminho)

    # 2. Lista para armazenar os códigos encontrados
    codigos_encontrados = []

    # 3. Para cada aba, procurar os códigos
    for aba_nome in abas_alvo:
        ws = wb[aba_nome]
        for linha in range(6, ws.max_row + 1):  # Começamos da linha 6 pra pular cabeçalho
            valor_celula = ws[f'B{linha}'].value
            if valor_celula and valor_celula.startswith('LMP'):
                codigos_encontrados.append(valor_celula)

    # 4. Retorna a lista de códigos encontrados
    return codigos_encontrados


















