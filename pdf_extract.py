import os
import re
import PyPDF2


def extrair_dados_pdf(caminho_pdf):
    # Abrir o PDF
    with open(caminho_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        # Extrair somente a primeira página
        primeira_pagina = reader.pages[0]
        texto = primeira_pagina.extract_text()

    dados_extraidos = {}

    if texto:
        # Dividir o texto em linhas
        linhas = texto.splitlines()

        # Procurar a linha que contém "Solicitante/Endereço:" ou "Applicant/Address:"
        for i, linha in enumerate(linhas):
            if "Solicitante/Endereço:" in linha or "Applicant/Address:" in linha:
                # O nome do solicitante é a próxima linha
                if i + 1 < len(linhas):
                    dados_extraidos['Nome_Solicitante'] = linhas[i + 1].strip()

                # Procurar o CNPJ nas próximas linhas
                for j in range(i + 1, min(i + 6, len(linhas))):  # procura nas próximas 5 linhas
                    cnpj_match = re.search(r'\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}', linhas[j])
                    if cnpj_match:
                        dados_extraidos['CNPJ'] = cnpj_match.group()
                        break
                break  # para depois que achar o solicitante

    return dados_extraidos


def pdf_extract(codigos_encontrados, base_path):
    resultados = []

    for codigo in codigos_encontrados:
        pasta_encontrada = None
        caminho_certificado = None
        dados_pdf = {}

        # Procurar pasta e PDF como na função anterior
        for nome_pasta in os.listdir(base_path):
            if nome_pasta.startswith(codigo):
                pasta_encontrada = nome_pasta
                break

        if pasta_encontrada:
            caminho_certificado = os.path.join(base_path, pasta_encontrada, '2 - Técnica', '1 - Certificado')

            if os.path.exists(caminho_certificado):
                for arquivo in os.listdir(caminho_certificado):
                    if arquivo.endswith('.pdf') and arquivo.startswith(codigo):
                        caminho_pdf = os.path.join(caminho_certificado, arquivo)
                        dados_pdf = extrair_dados_pdf(caminho_pdf)
                        status = 'PDF encontrado e dados extraídos'
                        break
                else:
                    status = 'PDF não encontrado'
            else:
                status = 'Pasta Certificado ausente'
        else:
            status = 'Pasta não encontrada'

        resultados.append((codigo, status, dados_pdf))

    return resultados

if __name__ == "__main__":
    base_path = r"C:\Users\marce\OneDrive - LMP Certificações\4. Projetos\2 - Ex\ALUTAL\181825"

    # Exemplo de códigos encontrados, você pode colocar os que você quiser testar
    codigos_encontrados = [
        "LMP 24.0190",
        "LMP 24.0191",
        "LMP 25.0001"
    ]

    resultados = pdf_extract(codigos_encontrados, base_path)

    for codigo, status, dados in resultados:
        print(f"Código: {codigo}")
        print(f"Status: {status}")
        print(f"Dados extraídos: {dados}")
        print("-" * 50)
