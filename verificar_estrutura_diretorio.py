def verificar_estrutura_diretorio(codigo, base_path):
    """
    Verifica se a estrutura de diretórios esperada existe para o código especificado.
    Retorna o caminho completo se existir, None caso contrário.
    """
    import os
    from logger import get_logger
    
    logger = get_logger(__name__)
    
    # Procurar pasta que contém o código (não apenas começa com ele)
    pasta_encontrada = None
    for pasta in os.listdir(base_path):
        # Verifica se o código está contido no nome da pasta
        if codigo in pasta:
            pasta_encontrada = pasta
            break
    
    if not pasta_encontrada:
        logger.warning(f"Pasta para o código {codigo} não encontrada em {base_path}")
        return None
    
    # Retorna o caminho da pasta encontrada
    caminho = os.path.join(base_path, pasta_encontrada)
    logger.info(f"Pasta encontrada para {codigo}: {caminho}")
    return caminho
