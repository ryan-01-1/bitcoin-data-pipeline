from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

import os
from dotenv import load_dotenv
import traceback
import logging

log_file = 'C:\\Users\\ryan.leite\\bitcoin-data-pipeline\\logs\\pipeline.log'

logging.basicConfig(
    filename=log_file,
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

load_dotenv()
api_key = os.getenv('API_KEY')

url = 'https://api.coingecko.com/api/v3/coins/markets'
params = {
    'vs_currency': 'usd',
    'order': 'market_cap_desc',
    'per_page': 20,
    'page': 1
}
headers = {'x_cg_demo_api_key': api_key}

caminho_csv_bruto = 'C:\\Users\\ryan.leite\\bitcoin-data-pipeline\\data\\raw\\bitcoin_bruto.csv'
caminho_csv_tratado = 'C:\\Users\\ryan.leite\\bitcoin-data-pipeline\\data\\processed\\bitcoin_tratado.csv'

def main():
  try:
    logging.info('===== INICIANDO PIPELINE =====')
    ## ETAPA 1 - Extract
    logging.info('Iniciando a extração dos dados')
    df_bruto = extract_data(url, params, headers)

    if df_bruto.empty:
      logging.warning('DataFrame está vazio')
      return

    logging.info('Extração finalizada')

    ## ETAPA 2 - Transform
    logging.info('Iniciando a transformação dos dados')
    df_tratado = transform_data(df_bruto)
    logging.info('Transformação finalizada')

    ## ETAPA 3 - Load
    logging.info('Iniciando o carregamento dos dados')
    load_data(df_bruto, caminho_csv_bruto)
    load_data(df_tratado, caminho_csv_tratado)
    logging.info('Carregamento finalizado')

    logging.info('===== PIPELINE FINALIZADO =====')
  except Exception as e:
    logging.error(f'Erro: {e}')
    logging.error(traceback.format_exc())

main()