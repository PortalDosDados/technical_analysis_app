#Importando bibliotecas necessárias
import yfinance as yf
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

#Definindo parametros
tickers = ['AAPL', 'MSFT', 'GOOGL']  # Lista de tickers para baixar
start_date = '2023-01-01'  # Data de início
end_date = '2023-12-31'    # Data de fim

#Função para baixar cotações

df = yf.download(tickers, start=start_date, end=end_date)

df_long = df.stack(level=1).reset_index()

df_long.columns = ['Date', 'Ticker', 'Open', 'Close', 'Volume']
#Exibindo as primeiras linhas do DataFrame resultante
print(df_long.head())
