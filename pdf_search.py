import os
from excel_load import carregar_codigos_excel

def procurar_pdfs(codigos_encontrados, base_path):
    resultados = []

    for codigo in codigos_encontrados:
        pasta_encontrada = None

        # Buscar nas pastas do diretório base
        for nome_pasta in os.listdir(base_path):
            # Verifica se a pasta começa com o código
            if nome_pasta.startswith(codigo):
                pasta_encontrada = nome_pasta
                break

        if not pasta_encontrada:
            status = 'Pasta não encontrada'
        else:
            # Monta caminho até 2 - Técnica\1 - Certificado
            caminho_certificado = os.path.join(base_path, pasta_encontrada, '2 - Técnica', '1 - Certificado')
            if not os.path.exists(caminho_certificado):
                status = 'Pasta Certificado ausente'
            else:
                pdf_encontrado = None
                for arquivo in os.listdir(caminho_certificado):
                    # Procura PDF que começa com o código
                    if arquivo.endswith('.pdf') and arquivo.startswith(codigo):
                        pdf_encontrado = arquivo
                        break
                if pdf_encontrado:
                    status = 'PDF encontrado'
                else:
                    status = 'PDF não encontrado'

        resultados.append((codigo, status))

    return resultados

def main():
    # Caminho da planilha e base onde estão as pastas dos clientes
    pasta_base = r'E:\Programer\Python\Projetos\LMP\LMP_SPI_plan\Assets'
    planilha_caminho = os.path.join(pasta_base, 'Processos - SPI.xlsm')

    # Caminho correto do SharePoint
    sharepoint_base = r'C:\Users\marce\OneDrive - LMP Certificações\4. Projetos\2 - Ex\ALUTAL\181825'

    # Carregar os códigos da planilha
    codigos_encontrados = carregar_codigos_excel(planilha_caminho)

    # Exibir os códigos encontrados
    print("Códigos carregados da planilha:")
    for codigo in codigos_encontrados:
        print(f"- {codigo}")

    # Procurar PDFs
    resultados = procurar_pdfs(codigos_encontrados, sharepoint_base)

    # Exibir resultados
    print("\nResultados da busca de PDFs:")
    for codigo, status in resultados:
        print(f"Código {codigo}: {status}")

if __name__ == "__main__":
    main()
