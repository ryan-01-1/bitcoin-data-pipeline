import requests
import pandas as pd

def extract_data(url, params, headers):
  # Recebe os dados da api
  response = requests.get(url, params=params, headers=headers)

  if response.status_code == 200:
    # Transforma a resposta da api em json
    data = response.json()

  else:
    raise Exception(f'Erro ao acessar API: {response.status_code}')

  # Transforma o json em um df(dataframe)
  df = pd.DataFrame(data)

  return df