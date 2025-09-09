# Projeto WebScraping de Criptomoedas

## Objetivo
Este projeto realiza a coleta de dados das principais criptomoedas no site "https://www.coingecko.com/pt"  através de WebScraping usando Selenium.  
Os dados extraídos incluem: Rank, Símbolo, Nome, Preço, Valor de Mercado, Variação 24h e Volume 24h, e são salvos em arquivo CSV.

---

## Estrutura de Pastas

WebScraping
│
├─ criptomoedas/
│ ├─ modelos.py # Modelos de dados
│ ├─ servico.py # Serviço principal de execução do WebScraping
│ ├─ repositorio_web.py # Módulo que realiza o scraping com Selenium
│ ├─ gravar_csv.py # Módulo para gravar os dados em CSV
│ └─ logger_config.py # Módulo de configuração do logging
│
├─ LOG/ # Pasta de Saida do log
├─ saida/ # Pasta de Saída do arquivo CSVs com a moedas coletadas
└─ executar_webscraping.py

## Instalação das Dependências

Com o python instalado abra o terminal (CMD) e digite:

pip install selenium webdriver-manager

### Como Executar

Garanta que o Python esteja instalado com as dependencias necessárias.

Abra o terminal na pasta do projeto.

Execute o script principal:

python executar_webscraping.py


### Ao final, os arquivos serão gerados nas pastas correspondentes:

CSV com os dados: saida/moedas_extraidas_webscraping.csv

Log da execução: pasta LOG/ com nome log_dd_mm_aaaa_hhMMss.txt