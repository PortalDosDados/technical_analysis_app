#Importar as bibliotecas necessárias
import yfinance as yf
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

# Definir parametros
ticker = "BBSE3.SA"
start_date = "2020-01-01"
end_date = "2023-01-01"

# Baixar dados históricos
df = yf.download(ticker, start=start_date, end=end_date)



