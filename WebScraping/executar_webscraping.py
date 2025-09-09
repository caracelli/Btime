import os
import logging
logging.getLogger("WDM").setLevel(logging.ERROR)  # Suprime mensagens do WebDriver Manager
logging.getLogger("selenium").setLevel(logging.WARNING)
from criptomoedas.servico import ServicoDados
from criptomoedas.logger_config import *
from datetime import datetime

if __name__ == "__main__":
    try:
        # Cria pastas de saída
        os.makedirs("saida", exist_ok=True)
        arquivo_saida = "saida/moedas_extraidas_webscraping.csv"

        logging.info("Início da execução WebScraping")

        servico = ServicoDados()

        # Chamada do WebScraping com navegador visível
        moedas = servico.executar_webscraping(arquivo_saida, quantidade=10)

        if moedas:
            logging.info(f"Extração concluída. {len(moedas)} moedas salvas em {arquivo_saida}")
        else:
            logging.warning("Nenhuma moeda foi coletada na Extração.")

        # Mostra no console onde está o arquivo de log
        log_pasta = "log"
        log_arquivos = os.listdir(log_pasta)
        log_arquivos = [f for f in log_arquivos if f.endswith(".txt")]
        if log_arquivos:
            # Pega o log mais recente
            log_arquivos.sort()
            log_atual = os.path.join(log_pasta, log_arquivos[-1])
            print(f"Arquivo de log gerado em: {log_atual}")
        else:
            print("Nenhum arquivo de log encontrado.")

    except Exception as e:
        logging.error(f"Falha na execução principal: {e}")
