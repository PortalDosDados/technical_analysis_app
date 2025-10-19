#Importando as bibliotecas necessárias
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Definindo o ticker e o período de análise
ticker = input(f'Entre com o ticker da ação (ex: BBSE.SA):')
date_start = input('Qual a data do início a ser analisado? (ex: YYYY-MM-DD): ')
date_end = input('Qual a data final? (ex: YYYY-MM-DD): ')

df = yf.download(ticker, start=date_start, end=date_end)



print(df.head()) 

plt.figure(figsize=(12, 6))
