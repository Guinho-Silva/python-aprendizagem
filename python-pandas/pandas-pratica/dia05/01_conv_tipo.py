#%%

import pandas as pd
#%%

df = pd.read_csv("../arquivos/clientes.csv", sep=';')


df['qtdePontos'].dtype
#%%

#Convertendo para float

#astype converte o tipo da coluna


df['qtdePontos'].astype(float)

#%%

#Convertendo datas = pd.to_datetime, caso haja uma data quebrada, devemos usar o replace

pd.to_datetime(df['DtCriacao'])

#%%
'''Usando o replace, nele devemos usar o valor antigo como chave e o novo como valor (dicionario)'''

df["DtCriacao"] = df['DtCriacao'].replace({"0000-00-00 00:00.000": "2026-02-14 09:00.000"})

df['DtCriacao']

#%%

df['DtCriacao'].dt.month