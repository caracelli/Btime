from criptomoedas.repositorio_web import RepositorioWeb
from criptomoedas.gravar_csv import gravar_csv
import logging

class ServicoDados:
    def executar_webscraping(self, arquivo_saida: str, quantidade: int = 10):
        logging.info("Início do Web Scraping")
        try:
            repositorio = RepositorioWeb(modo_oculto=True)
            moedas = repositorio.buscar_moedas_topo(quantidade=quantidade)
            if moedas:
                gravar_csv(moedas, arquivo_saida)
            repositorio.fechar()
            return moedas
        except Exception as e:
            logging.error(f"Falha ao coletar moedas: {e}")
            return []
