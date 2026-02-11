#%%

import pandas as pd


df_clientes = pd.read_csv("clientes.csv")

df_clientes

#%%

#Verifica se os dados foram carregados corretamente limitando pelas 5 primeiras linhas
df_clientes.head(n=10)

#%%
#Retorna as ultimas linhas de um dataSet
df_clientes.tail(n=10)

#%%

#Ver os dados "Sorteados" para verificar se os dados estão corretos

df_clientes.sample(n=10)
#%%

#Retorna quantas linhas e colunas tem em um dataset (shape é  um atributo)

df_clientes.shape

#%%

#Retorna os nomes das colunas de um dataset

df_clientes.columns
#%%

#Retorna os indicies de uma dataframe

df_clientes.index

#%%

#Retorna as informações de um dataframe

df_clientes.info()

#%%

#Retorna a quantidade real  da memoria sendo usada

df_clientes.info(memory_usage='deep')

#%%

# Retorna uma serie mostrando os tipos de cada coluna

df_clientes.dtypes["idCliente"]
#%%


