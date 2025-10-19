#Importando as bibliotecas necessárias
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Definindo o ticker e o período de análise
ticker = input(f'Entre com o ticker da ação (ex: BBSE3.SA):')
date_start = input('Qual a data do início a ser analisado? (ex: YYYY-MM-DD): ')
date_end = input('Qual a data final? (ex: YYYY-MM-DD): ')

df = yf.download(ticker, start=date_start, end=date_end)

# Se tiver MultiIndex, pega o último nível (nomes reais)
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(-1)

df.reset_index(inplace=True) # type: ignore

df['Ticker'] = ticker  # type: ignore

df = df.rename(columns={
    'Date': 'Data',
    'Open': 'Abertura',
    'High': 'Máxima',
    'Low': 'Mínima',
    'Close': 'Fechamento',
    'Adj Close': 'Fechamento Ajustado',
    'Volume': 'Volume'
})  

# Selecionando apenas as colunas que você quer
df_long = df[['Ticker', 'Data', 'Abertura', 'Fechamento', 'Volume']]

# Exibindo resultado
print(df_long.head())