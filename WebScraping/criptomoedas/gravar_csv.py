import csv
from criptomoedas.modelos import Moeda
import logging

def gravar_csv(moedas: list, arquivo: str):
    """
    Grava a lista de moedas em arquivo CSV.
    """
    try:
        with open(arquivo, mode='w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(['Rank', 'Símbolo', 'Nome', 'Preço', 'Valor de Mercado', 'Variação 24h', 'Volume 24h'])
            for moeda in moedas:
                writer.writerow([
                    moeda.rank,
                    moeda.simbolo,
                    moeda.nome,
                    moeda.preco,
                    moeda.valor_mercado,
                    moeda.variacao_24h,
                    moeda.volume_24h
                ])
        logging.info(f"Arquivo CSV gerado: {arquivo}")
    except Exception as e:
        logging.error(f"Erro ao gravar CSV: {e}")
