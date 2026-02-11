#%%
#RENOMEANDO COLUNAS

import pandas as pd

df = pd.read_csv("../arquivos/transacoes.csv", sep=';')

df
#%%

# Retorna a quantidade de linhas e colunas 
df.shape

#%%

#retorna quanto de memoria esta sendo usado

df.info(memory_usage='deep')
#%%

#retorna o tipo de cada coluna

df.dtypes

#%%

#Renomear coluna
renamed_columns ={"QtdePontos": "QtPontos", "DescSistemaOrigem": "SistemaOrigem"

}
df.rename(columns=renamed_columns)

# A chave do dicionario vai ser o nome antigo, e o valor atribuido à ela, vai ser o novo 

'df.rename(columns=renamed_columns, inplace=True)#Fará com que o dataset seja realmente alterado'

#%%

df[["IdCliente","QtdePontos"]]

#%%

# SELECT * FROM df

df

#%%

#SELECT IdCliente FROM df

df[["IdCliente"]]

#%%
#SELECT IdCliente, QtdePontos FROM df LIMIT 5

df[["IdCliente", "QtdePontos"]].tail(5)

#%%

# SELECT IdCliente, idTransacao, QtdePontos FROM df LIMIT 5

df[["IdCliente", "IdTransacao", "QtdePontos"]].head(5)

#%%
#Ordena em ordem alfabetica

colunas = list(df.columns)

colunas.sort()
colunas

df = df[colunas]
df