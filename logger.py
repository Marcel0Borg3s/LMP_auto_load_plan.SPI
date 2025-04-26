
"""
Módulo de logging para o projeto LMP_auto_load_plan.SPI
"""
import logging
import os
from datetime import datetime

# Configurar o logger
log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, f"execucao_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")

# Configurar o formato do log
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

def get_logger(name):
    """Retorna um logger configurado para o módulo especificado"""
    return logging.getLogger(name)