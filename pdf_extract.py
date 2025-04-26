import os
import re
import PyPDF2
from config import BASE_PATH
from logger import get_logger
from utils import verificar_estrutura_diretorio

logger = get_logger(__name__)


def pdf_extract(codigos_encontrados, base_path):
    """
    Processa uma lista de códigos, buscando e extraindo dados dos PDFs correspondentes.
    Retorna uma lista de tuplas (codigo, status, dados_pdf).
    """
    import os
    from logger import get_logger

    logger = get_logger(__name__)
    logger.info(f"Iniciando extração de PDFs para {len(codigos_encontrados)} códigos")
    logger.info(f"Usando caminho base: {base_path}")

    resultados = []

    for codigo in codigos_encontrados:
        logger.info(f"Processando código: {codigo}")

        # Verificar estrutura de diretórios
        from utils import verificar_estrutura_diretorio
        caminho_pasta = verificar_estrutura_diretorio(codigo, base_path)
        if not caminho_pasta:
            resultados.append((codigo, "Pasta não encontrada", {}))
            continue

        # Procurar arquivo PDF diretamente na pasta encontrada
        pdf_encontrado = None
        for arquivo in os.listdir(caminho_pasta):
            if arquivo.endswith('.pdf') and codigo in arquivo:
                pdf_encontrado = arquivo
                break

        if not pdf_encontrado:
            logger.warning(f"PDF não encontrado para {codigo} em {caminho_pasta}")
            resultados.append((codigo, "PDF não encontrado", {}))
            continue

        # Extrair dados do PDF
        caminho_pdf = os.path.join(caminho_pasta, pdf_encontrado)
        logger.info(f"PDF encontrado: {caminho_pdf}")

        # Importar a função extrair_dados_pdf
        from pdf_extract import extrair_dados_pdf
        dados_pdf = extrair_dados_pdf(caminho_pdf)

        if dados_pdf and 'Nome_Solicitante' in dados_pdf and 'CNPJ' in dados_pdf:
            logger.info(f"Dados extraídos com sucesso para {codigo}")
            resultados.append((codigo, "PDF encontrado e dados extraídos", dados_pdf))
        else:
            logger.warning(f"Falha ao extrair dados para {codigo}")
            resultados.append((codigo, "Falha na extração de dados", {}))

    return resultados