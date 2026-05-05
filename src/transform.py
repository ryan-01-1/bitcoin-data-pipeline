from datetime import datetime
import pandas as pd

def transform_data(df):
  # Cria a nova coluna "Data da coleta" com a data e hora em que os dados foram coletados
  df['data_da_coleta'] = datetime.now().replace(second=0, microsecond=0)

  # Mudando o tipo da coluna
  df['market_cap'] = df['market_cap'].astype(float)

  # Filtrando para pegar só as colunas importantes e dpois tirando o que é nulo
  df_final = df[['id', 'name', 'current_price', 'market_cap', 'price_change_percentage_24h', 'data_da_coleta']]
  df_final = df_final.dropna()

  # Renomeando as colunas
  df_final = df_final.rename(columns={
      'name': 'nome',
      'current_price': 'preco_atual',
      'market_cap': 'capitalizacao_mercado',
      'price_change_percentage_24h': 'variacao_preco_24h'
  })

  return df_final