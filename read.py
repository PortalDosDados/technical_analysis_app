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


'''

# Importar dados de CSV em formato longo
data = pd.read_csv('cotacoes_long_format.csv')

# Alterar formato da data
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Formatar data para dia/mês/ano
data['Date'] = data['Date'].dt.strftime('%d/%m/%Y')

# Renomear colunas
data = data.rename(columns={
    'Ticker': 'ticker',
    'Date': 'data',
    'Close': 'fechamento',
    'Open': 'abertura',
    'Volume': 'volume'
})

data['id'] = range(1, len(data) + 1)

data = data[['id','ticker', 'data', 'abertura', 'fechamento', 'volume']]

data.to_excel('cotacoes_formatado_2.xlsx', index=False)

#print(data.head())

'''

# Importar dados de Excel
data_1 = pd.read_excel('cotacoes_formatado.xlsx',)
data_2 = pd.read_excel('cotacoes_formatado_2.xlsx',)

# Concatenar os dois dataframes
data_concat = pd.concat([data_1, data_2], ignore_index=True)

# Contar número de linhas antes de remover duplicatas
print(f"Número de linhas antes de remover duplicatas: {len(data_concat)}")

# Contar número de duplicatas
num_duplicatas = data_concat.duplicated(subset=['ticker', 'data']).sum()

print(f"Número de duplicatas encontradas: {num_duplicatas}")

# Remover duplicatas
#data_concat = data_concat.drop_duplicates(subset=['ticker', 'data'], keep='first').reset_index(drop=True)

#print(data_concat.head())