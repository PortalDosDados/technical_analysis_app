import yfinance as yf
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


tickers = 'BBAS3.SA', 'VALE3.SA'
start_date = '2000-01-01'
end_date = '2025-10-19'

df = yf.download(tickers, start=start_date, end=end_date)

# Convertendo para formato longo
df_long = df.stack(level=1).reset_index()

df_long = df_long.rename(columns={
    'Date': 'Data',
    'Open': 'Abertura',
    'Close': 'Fechamento',
    'High': 'Máxima',
    'Low': 'Mínima',
    'Volume': 'Volume'
})

df_long = df_long[['Data', 'Ticker', 'Abertura', 'Fechamento', 'Volume']]


df_long.to_csv('cotacoes.csv', index=False)


#print(df_long.head())

