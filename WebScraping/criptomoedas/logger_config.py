import logging
import os
from datetime import datetime

os.makedirs("log", exist_ok=True)
# define o nome do arquivo de log
log_nome = datetime.now().strftime("log/log_%d_%m_%Y_%H%M%S.txt")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_nome, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
