import csv
import logging
from criptomoedas.modelos import Moeda

def escrever_moedas_csv(caminho: str, moedas: list[Moeda]):
    """
    Grava a lista de moedas em arquivo CSV.
    """
    try:
        logging.info(f"Início da gravação do CSV: {caminho}")
        with open(caminho, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo, delimiter=';')
            escritor.writerow(["Rank", "Simbolo", "Nome", "Preco", "Valor Mercado", "Variacao 24h", "Volume 24h"])
            for moeda in moedas:
                escritor.writerow([
                    moeda.rank, 
                    moeda.simbolo.upper(), 
                    moeda.nome, 
                    moeda.preco, 
                    moeda.valor_mercado, 
                    moeda.variacao_24h, 
                    moeda.volume_24h
                ])
                logging.debug(f"Moeda gravada no CSV: {moeda.simbolo} | {moeda.nome}")
        logging.info(f"Arquivo CSV gerado com sucesso: {caminho}")
    except Exception as e:
        logging.error(f"Erro ao gravar CSV: {e}", exc_info=True)
