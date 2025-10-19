#Import necessary libraries
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

# Function to fetch stock data
ticker = input(f'Entre com o ticker da ação (ex: BBSE.SA):')
date_start = input('Qual a data do início a ser analisado? (ex: YYYY-MM-DD): ')
date_end = input('Qual a data final? (ex: YYYY-MM-DD): ')

df = yf.download(ticker, start=date_start, end=date_end)

print(df.head()) 