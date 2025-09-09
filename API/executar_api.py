import os
import logging
from criptomoedas.servico import ServicoDados
from criptomoedas.logger_config import *

if __name__ == "__main__":
    try:
        # Cria pastas de saída
        os.makedirs("saida", exist_ok=True)
        arquivo_saida = "saida/moedas_extraidas_api.csv"

        logging.info("Início da execução do script API")

        servico = ServicoDados()
        moedas = servico.executar_api(arquivo_saida, quantidade=10)

        if moedas:
            logging.info(f"Execução concluída: {len(moedas)} moedas salvas.")
            print(f"Arquivo CSV gerado em: {arquivo_saida}")
        else:
            logging.warning("Nenhuma moeda foi coletada.")
    except Exception as e:
        logging.error(f"Falha na execução principal: {e}", exc_info=True)
