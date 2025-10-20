import pandas as pd
import matplotlib.pyplot as plt

'''

# Importar dados de CSV
data = pd.read_csv('cotacoes.csv')

#print(data.head())

# Criar coluna de id
data['id'] = range(1, len(data) + 1)

# Converter para datetime
data['Data'] = pd.to_datetime(data['Data'], errors='coerce')  # errors='coerce' transforma valores inválidos em NaT

# Agora formatar para exibição como dia/mês/ano
data['Data_formatada'] = data['Data'].dt.strftime('%d/%m/%Y')

# remover coluna antiga
data = data.drop(columns=['Data'])

# alterar titulo das colunas
data = data.rename(columns={
    'Ticker': 'ticker',
    'Data_formatada': 'data',
    'Abertura': 'abertura',
    'Fechamento': 'fechamento',
    'Volume': 'volume'
})

# Ordenar colunas
data = data[['id', 'ticker', 'data', 'abertura', 'fechamento', 'volume']]

#print(data.head())

data.to_excel('cotacoes_formatado.xlsx', index=False)
'''
# Importar dados de CSV em formato longo
data = pd.read_csv('cotacoes_long_format.csv')

# Alterar formato da data
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

data['Date'] = data['Date'].dt.strftime('%d/%m/%Y')

print(data.head())