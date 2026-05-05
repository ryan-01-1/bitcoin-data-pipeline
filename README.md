# Bitcoin Data Pipeline

Esse projeto implementa um pipeline ETL que coleta dados sobre criptomoedas de uma API do Coingecko, transforma, limpa, estrutura e depois salva em CSV para posteriormente ser analisado.

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

├── data/
   └── raw/			   # Arquivos JSON/CSV originais da API
   └── processed/		# CSVs limpos e tipados prontos para análise
├── logs/				# Registros de execução (info, warning, error)
├── src/
   └── extract			# Script de extração dos dados
   └── transform		# Script de transformação (limpeza, estruturação)
   └── load			   # Script que salva os dados em CSV
├── .env				   # Credenciais sensíveis (não versionar)
└── main.py				# Script principal de execução

## Como executar

1. Criar um arquivo `.env` com sua API key
   API_KEY=sua_chave_aqui
2. Instalar dependências:
   ``bash
   pip install requiriments.txt
3. Executar o arquivo main.py

## Exemplo de dados

|id|nome|preco\_atual|capitalizacao\_mercado|variacao\_preco\_24h|data\_da\_coleta|
|-|-|-|-|-|-|
|bitcoin|Bitcoin|65000|158899945403300|-1.1365|2026-05-04 13:25:00|



