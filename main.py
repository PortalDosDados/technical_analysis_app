#Import necessary libraries
import yfinance as yf
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Function to fetch stock data
ticker = input(f'Entre com o ticker da ação (ex: BBSE.SA):')
date_start = input('Qual a data do início a ser analisado? (ex: YYYY-MM-DD): ')
date_end = input('Qual a data final? (ex: YYYY-MM-DD): ')

