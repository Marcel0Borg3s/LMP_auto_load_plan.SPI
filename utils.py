"""
Funções utilitárias para o projeto LMP_auto_load_plan.SPI
"""
import os
from config import BASE_PATH, ESTRUTURA_CERTIFICADO
from logger import get_logger

logger = get_logger(__name__)


def verificar_estrutura_diretorio(codigo, base_path):
    """
    Verifica se a estrutura de diretórios esperada existe para o código especificado.
    Retorna o caminho completo se existir, None caso contrário.
    """
    logger = get_logger(__name__)
    # Procurar pasta que começa com o código
    pasta_encontrada = None
    for pasta in os.listdir(base_path):
        if codigo in pasta:
            pasta_encontrada = pasta
            break

    if not pasta_encontrada:
        logger.warning(f"Pasta para o código {codigo} não encontrada em {base_path}")
        return None

    # Procurar subpastas
    for subpasta in ESTRUTURA_CERTIFICADO:
        caminho = os.path.join(base_path, pasta_encontrada, subpasta)
        if not os.path.exists(caminho):
            logger.warning(f"Subpasta {subpasta} não encontrada em {caminho}")
            return None

        if pasta.startswith(codigo):
            pasta_encontrada = pasta
            break

    if not pasta_encontrada:
        logger.warning(f"Pasta para o código {codigo} não encontrada em {BASE_PATH}")
        return None

    # Construir o caminho completo
    caminho = os.path.join(BASE_PATH, pasta_encontrada)
    for subpasta in ESTRUTURA_CERTIFICADO:
        caminho = os.path.join(caminho, subpasta)
        if not os.path.exists(caminho):
            logger.warning(f"Subpasta {subpasta} não encontrada em {caminho}")
            return None

    logger.info(f"Estrutura de diretórios válida para {codigo}: {caminho}")
    return caminho