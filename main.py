from excel_load import carregar_codigos_excel
from pdf_extract import pdf_extract
from write_excel_file import preencher_planilhas
import os
from config import PLANILHA_CAMINHO, BASE_PATH
from logger import get_logger

logger = get_logger(__name__)


def main():
    """Função principal do programa"""
    logger.info("Iniciando processamento")

    # Verificar se os caminhos existem
    if not os.path.exists(PLANILHA_CAMINHO):
        logger.error(f"Planilha não encontrada: {PLANILHA_CAMINHO}")
        return

    if not os.path.exists(BASE_PATH):
        logger.error(f"Caminho base não encontrado: {BASE_PATH}")
        return

    # Teste para ver as pastas que existem
    logger.info("Pastas que existem em base_path:")
    for pasta in os.listdir(BASE_PATH):
        logger.info(f"  - {pasta}")

    # Continua seu código normal
    logger.info(f"Carregando códigos da planilha: {PLANILHA_CAMINHO}")
    codigos_encontrados = carregar_codigos_excel(PLANILHA_CAMINHO)
    logger.info(f"Encontrados {len(codigos_encontrados)} códigos na planilha")

    logger.info("Extraindo dados dos PDFs")
    resultados = pdf_extract(codigos_encontrados, BASE_PATH)

    # Processar resultados
    for codigo, status, dados_pdf in resultados:
        logger.info(f"{codigo} - {status}")

        if status == "PDF encontrado e dados extraídos":
            logger.info(f"Código: {codigo}")
            logger.info(f"Dados extraídos: {dados_pdf}")

            # Preencher a planilha
            sucesso = preencher_planilhas(PLANILHA_CAMINHO, dados_pdf, codigo)
            if sucesso:
                logger.info(f"Planilha atualizada com sucesso para {codigo}")
            else:
                logger.warning(f"Falha ao atualizar planilha para {codigo}")

    logger.info("Processamento concluído")


if __name__ == "__main__":
    main()
