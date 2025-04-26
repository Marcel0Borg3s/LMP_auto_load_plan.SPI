from excel_load import codigos_encontrados
from pdf_search import procurar_pdfs

base_path = r'C:\Users\marce\OneDrive - LMP Certificações\4. Projetos\2 - Ex\ALUTAL\181825'

resultados = procurar_pdfs(codigos_encontrados, base_path)

# Agora salva no Excel ou imprime, etc
for codigo, status in resultados:
    print(f'{codigo} - {status}')
