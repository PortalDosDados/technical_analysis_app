import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import warnings
warnings.filterwarnings("ignore")

# Definir parâmetros
tickers = ['BBSE3.SA']
start_date = '2020-01-01'
end_date = '2025-10-19'

# Baixar dados históricos
df = yf.download(tickers, start=start_date, end=end_date)

# Transformar MultiIndex em formato longo (tickers como coluna)
df_long = df.stack(level=1).reset_index() #type: ignore

# Renomear colunas para português e substituir 'Price' por 'ID'
df_long = df_long.rename(columns={
    'level_1': 'Ticker',
    'Open': 'Abertura',
    'Close': 'Fechamento',
    'Volume': 'Volume',
    'Date': 'Data'
})

# Substituir a coluna 'Price' por uma coluna 'Id' sequencial
df_long['Id'] = range(1, len(df_long) + 1)

# Selecionar apenas as colunas desejadas e na ordem certa
df_long = df_long[['Id', 'Ticker', 'Data', 'Abertura', 'Fechamento', 'Volume']]

# Salvar em CSV
df_long.to_csv('dados_historicos.csv', index=False)

# Exibir os primeiros registros
#print(df_long.head())

'''
# Plotar os dados de fechamento
plt.figure(figsize=(12, 6))
for ticker in tickers:
    subset = df_long[df_long['Ticker'] == ticker]
    plt.plot(subset['Data'], subset['Fechamento'], label=ticker)
plt.title(f'Preços de Fechamento Históricos - {tickers[0]}')
plt.ylabel('Preço de Fechamento (R$)')
plt.grid(True)
plt.legend()
plt.show()
'''