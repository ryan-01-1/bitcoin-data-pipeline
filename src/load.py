import os
import pandas as pd

def load_data(df, caminho_csv):
  # Verifica se existe o arquivo do argumento
  if os.path.exists(caminho_csv):
    df_existente = pd.read_csv(caminho_csv)

    # Concatena e remove o que é duplicata
    df = pd.concat([df_existente, df])
    df = df.drop_duplicates(subset=['id', 'data_da_coleta'], keep= 'last')

  # Salva o arquivo
  df.to_csv(caminho_csv, index=False)