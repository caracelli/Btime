import requests
from typing import List
from criptomoedas.modelos import Moeda
import logging

class RepositorioAPI:
    BASE = "https://api.coingecko.com/api/v3"

    def _formata_numero(self, valor: float) -> str:
        """Formata número para padrão brasileiro (1.234,56)"""
        try:
            return f"{float(valor or 0.0):,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
        except Exception as e:
            logging.error(f"Erro ao formatar número {valor}: {e}", exc_info=True)
            return "0,00"

    def buscar_moedas_topo(self, quantidade: int = 10, moeda_referencia: str = "usd") -> List[Moeda]:
        logging.info(f"Iniciando coleta das {quantidade} principais moedas via API")
        moedas = []
        try:
            url = f"{self.BASE}/coins/markets"
            parametros = {
                "vs_currency": moeda_referencia,
                "order": "market_cap_desc",
                "per_page": quantidade,
                "page": 1,
                "price_change_percentage": "24h"
            }

            resposta = requests.get(url, params=parametros, timeout=60)
            resposta.raise_for_status()
            dados = resposta.json()
            logging.info(f"API retornou {len(dados)} moedas")

            for item in dados:
                try:
                    rank = item.get("market_cap_rank") or 0
                    simbolo = (item.get("symbol") or "").upper()
                    nome = item.get("name") or ""
                    preco = self._formata_numero(item.get("current_price"))
                    valor_mercado = self._formata_numero(item.get("market_cap"))
                    variacao_24h = self._formata_numero(item.get("price_change_percentage_24h"))
                    volume_24h = self._formata_numero(item.get("total_volume"))

                    logging.info(f"{rank} | {simbolo} | {nome} | Preço: {preco} | Valor Mercado: {valor_mercado} | Variação 24h: {variacao_24h} | Volume 24h: {volume_24h}")

                    moedas.append(Moeda(
                        rank=rank,
                        simbolo=simbolo,
                        nome=nome,
                        preco=preco,
                        valor_mercado=valor_mercado,
                        variacao_24h=variacao_24h,
                        volume_24h=volume_24h
                    ))
                except Exception as e:
                    logging.error(f"Erro ao processar moeda {item}: {e}", exc_info=True)
            logging.info("Coleta via API finalizada com sucesso.")
            return moedas
        except requests.RequestException as e:
            logging.error(f"Falha na requisição à API: {e}", exc_info=True)
            return []
        except Exception as e:
            logging.error(f"Falha ao processar dados da API: {e}", exc_info=True)
            return []
