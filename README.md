# Bitcoin Data Pipeline

Esse projeto implementa um pipeline ETL que coleta dados sobre criptomoedas de uma API da Coingecko, transforma, limpa, estrutura e depois salva em CSV para posteriormente ser analisado.

## Tecnologias

* Python 3.10+
* Python dot-env
* Pandas
* Requests

## Pipeline

* Extract: coleta dados da API
* Transform: limpa e estrutura os dados
* Load: salva os dados em CSV

## Estrutura

```bash
bitcoin-data-pipeline/
├── data/
│   ├── raw/         # Dados brutos da API
│   └── processed/   # Dados tratados prontos para análise
├── logs/            # Logs de execução (info, warning, error)
├── src/
│   ├── extract.py   # Extração dos dados
│   ├── transform.py # Limpeza e transformação
│   └── load.py      # Salvamento dos dados
├── .env             # Variáveis de ambiente (não versionar)
└── main.py          # Script principal
```

## Como executar

1. Criar um arquivo `.env` na pasta raiz do projeto com sua API key<br>
```bash
API_KEY=sua_chave_aqui
```
2. Instalar dependências:<br>
````bash
pip install -r requirements.txt
````
3. Executar o arquivo main.py

## Exemplo de dados

|id|nome|preco\_atual|capitalizacao\_mercado|variacao\_preco\_24h|data\_da\_coleta|
|-|-|-|-|-|-|
|bitcoin|Bitcoin|65000|158899945403300|-1.1365|2026-05-04 13:25:00|



