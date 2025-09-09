import os
import time
from typing import List
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from criptomoedas.modelos import Moeda
import logging
from criptomoedas.logger_config import *
import sys
from contextlib import contextmanager

# Suprime mensagens de erro do log
@contextmanager
def suprimir_stdout_stderr():
    with open(os.devnull, "w") as devnull:
        old_stdout, old_stderr = sys.stdout, sys.stderr
        try:
            sys.stdout, sys.stderr = devnull, devnull
            yield
        finally:
            sys.stdout, sys.stderr = old_stdout, old_stderr
            
            
class RepositorioWeb:
    def __init__(self, modo_oculto: bool = True, tempo_espera: float = 3.0):
        try:
            # Argumentos de inicialização do Chrome
            opcoes = Options()
            opcoes.add_argument("--headless=new") # comente essa linha caso queira ver o navegador abrindo
            opcoes.add_argument("--disable-gpu")
            opcoes.add_argument("--disable-software-rasterizer")
            opcoes.add_argument("--enable-unsafe-swiftshader")
            opcoes.add_argument("--no-sandbox")
            opcoes.add_argument("start-maximized")
            opcoes.add_argument("user-agent=Mozilla/5.0")
            opcoes.add_argument("--log-level=3")                # Suprime logs (0=INFO, 3=FATAL)
            opcoes.add_experimental_option("excludeSwitches", ["enable-logging"])  # Oculta logs no console

            # verifica a pasta de log
            os.makedirs("log", exist_ok=True)
            # instala o driver do chrome caso não exista
            servico = Service(
                ChromeDriverManager().install(),
                log_path="log/chromedriver.log"
            )
            self._driver = webdriver.Chrome(service=servico, options=opcoes)
            self._tempo_espera = tempo_espera
            logging.info("Navegador iniciado com sucesso")
        except Exception as e:
            logging.error(f"Falha ao iniciar o navegador: {e}")
            raise

    def buscar_moedas_topo(self, quantidade: int = 10) -> List[Moeda]:
        moedas = []
        try:
            # inicia a navegação no portal 
            url = "https://www.coingecko.com/pt"
            self._driver.get(url)
            #aguarda o carregamento da página
            time.sleep(self._tempo_espera)

            for idx in range(1, quantidade + 1):
                try:
                    # XPath de cada célula da linha idx
                    posicao_xpath = f"/html/body/div[2]/main/div/div[5]/table/tbody/tr[{idx}]/td[2]"
                    nome_xpath = f"/html/body/div[2]/main/div/div[5]/table/tbody/tr[{idx}]/td[3]/a/div/div"
                    simbolo_xpath = f"/html/body/div[2]/main/div/div[5]/table/tbody/tr[{idx}]/td[3]/a/div/div/div"
                    preco_xpath = f"/html/body/div[2]/main/div/div[5]/table/tbody/tr[{idx}]/td[5]/span"
                    variacao_xpath = f"/html/body/div[2]/main/div/div[5]/table/tbody/tr[{idx}]/td[6]/span"
                    volume_xpath = f"/html/body/div[2]/main/div/div[5]/table/tbody/tr[{idx}]/td[10]/span"
                    valor_mercado_xpath = f"/html/body/div[2]/main/div/div[5]/table/tbody/tr[{idx}]/td[11]/span"

                    # Captura os elementos
                    posicao_el = self._driver.find_element("xpath", posicao_xpath).text
                    nome_completo = self._driver.find_element("xpath", nome_xpath).text
                    simbolo_el = self._driver.find_element("xpath", simbolo_xpath).text
                    preco_el = self._driver.find_element("xpath", preco_xpath).text
                    variacao_el = self._driver.find_element("xpath", variacao_xpath).text
                    volume_el = self._driver.find_element("xpath", volume_xpath).text
                    valor_mercado_el = self._driver.find_element("xpath", valor_mercado_xpath).text

                    # Remove símbolo do nome
                    if nome_completo.endswith(simbolo_el):
                        nome_el = nome_completo[: -len(simbolo_el)].strip()
                    else:
                        nome_el = nome_completo.strip()

                    # Converte os valores 
                    try:
                        posicao = int(posicao_el.split()[0])
                    except ValueError:
                        posicao = idx
                    try:
                        preco = preco_el.replace("$","").replace("--","0").replace("US ","")
                    except ValueError:
                        preco = 0.0
                    try:
                        variacao_24h = variacao_el.replace("%","").replace("--","0").replace("US ","")
                    except ValueError:
                        variacao_24h = 0.0
                    try:
                        volume_24h = volume_el.replace("$","").replace("--","0").replace("US ","")
                    except ValueError:
                        volume_24h = 0.0
                    try:
                        valor_mercado = valor_mercado_el.replace("$","").replace("--","0").replace("US ","")
                    except ValueError:
                        valor_mercado = 0.0

                    moedas.append(Moeda(posicao, simbolo_el, nome_el, preco, valor_mercado, variacao_24h, volume_24h))

                    # Exibe no console os dados capturados
                    logging.info(f"{posicao} | {simbolo_el} | {nome_el} | Preço: {preco} | Valor Mercado: {valor_mercado} | Variação 24h: {variacao_24h} | Volume 24h: {volume_24h}")
        
                except Exception as e:
                    logging.error(f"Erro ao processar linha {idx}: {e}")
                    continue

            return moedas

        except Exception as e:
            logging.error(f"Falha ao buscar moedas: {e}")
            return []

    def fechar(self):
        try:
            self._driver.quit()
            logging.info("Navegador fechado")
        except Exception as e:
            logging.error(f"Falha ao fechar o navegador: {e}")
