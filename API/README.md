# Projeto API de captura de Criptomoedas

##Objetivo
Este projeto realiza a coleta de dados das principais criptomoedas utilizando a API do CoinGecko (https://api.coingecko.com/api/v3).
Os dados extraídos incluem: Rank, Símbolo, Nome, Preço, Valor de Mercado, Variação 24h e Volume 24h, e são salvos em arquivo CSV.

---

## Estrutura de Pastas

API
│
├─ criptomoedas/
│ ├─ modelos.py # Modelos de dados
│ ├─ servico.py # Serviço principal de execução da coleta via API
│ ├─ repositorio_api.py # Módulo que realiza a requisição e processa os dados da API
│ ├─ gravar_csv.py # Módulo para gravar os dados em CSV
│ └─ logger_config.py # Módulo de configuração do logging
│
├─ LOG/ # Pasta de saída dos logs
├─ saida/ # Pasta de saída dos arquivos CSV com as moedas coletadas
└─ executar_api.py # Script principal para executar a coleta via API

# Instalação das Dependências

Com o python instalado abra o terminal (CMD) e digite:

pip install requests

### Como Executar

Garanta que o Python esteja instalado com as dependencias necessárias.

Abra o terminal na pasta do projeto.

Execute o script principal:

python executar_api.py

### Ao final, os arquivos serão gerados nas pastas correspondentes:

CSV com os dados: saida/moedas_extraidas_api.csv

Log da execução: pasta LOG/ com nome log_dd_mm_aaaa_hhMMss.txt

O console exibirá o caminho do log gerado, assim você sabe exatamente onde encontrá-lo.
