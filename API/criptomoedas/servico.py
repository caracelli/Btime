from criptomoedas.repositorio_api import RepositorioAPI
from criptomoedas.gravar_csv import escrever_moedas_csv
import logging

class ServicoDados:
    def executar_api(self, caminho_saida: str, quantidade: int = 10):
        logging.info("Início da coleta via API")
        repo = RepositorioAPI()
        try:
            moedas = repo.buscar_moedas_topo(quantidade=quantidade)
            if moedas:
                try:
                    escrever_moedas_csv(caminho_saida, moedas)
                    print("Moedas salvas com sucesso.")
                    logging.info(f"Coleta via API concluída: {len(moedas)} moedas salvas em {caminho_saida}")
                except Exception as e:
                    logging.error(f"Erro ao gravar CSV: {e}", exc_info=True)
            else:
                logging.warning("Nenhuma moeda foi coletada via API.")
            return moedas
        except Exception as e:
            logging.error(f"Falha no serviço API: {e}", exc_info=True)
            return []
