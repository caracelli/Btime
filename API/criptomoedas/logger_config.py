import logging
import os
from datetime import datetime

try:
    os.makedirs("log", exist_ok=True)
    timestamp = datetime.now().strftime("%d_%m_%Y_%H%M%S")
    arquivo_log = f"log/log_{timestamp}.txt"

    logging.basicConfig(
        filename=arquivo_log,
        filemode="w",
        format="%(asctime)s [%(levelname)s] %(message)s",
        level=logging.INFO,
    )
    logging.info("Logger configurado com sucesso.")
except Exception as e:
    print(f"Falha ao configurar logger: {e}")
