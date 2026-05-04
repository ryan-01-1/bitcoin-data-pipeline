# Bitcoin Data Pipeline

Coleta dados sobre criptomoedas de uma API do Coingecko, transforma, limpa e estrutura os dados, depois salva em CSV para análise posterior.

## Tecnologias

* Python 3.10+
* Pandas
* Requests
* Logging

## Pipeline

* Extract: coleta dados da API
		|
		V
* Transform: limpa e estrutura os dados
		|
		V
* Load: salva os dados em CSV

## Estrutura

├── data/
│   ├── raw/         # Arquivos JSON/CSV originais da API
│   └── processed/   # CSVs limpos e tipados prontos para análise
├── logs/            # Registros de execução (info, warning, error)
├── .env             # Credenciais sensíveis (não versionar)
└── pipeline.ipynb   # Script principal de execução

## Como executar

1. Criar um arquivo `.env` com sua API key
   API_KEY=sua_chave_aqui
2. Instalar dependências:
   ``bash
   pip install python-dotenv requests pandas
3. Executar o notebook

## Exemplo de dados

|id|nome|preco\_atual|capitalizacao\_mercado|variacao\_preco\_24h|data\_da\_coleta|
|-|-|-|-|-|-|
|bitcoin|Bitcoin|65000|158899945403300|-1.1365|2026-05-04 13:25:00|



