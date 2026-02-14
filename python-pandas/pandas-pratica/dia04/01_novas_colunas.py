#%%

import pandas as pd

import numpy as np

df= pd.read_csv("../arquivos/clientes.csv", sep=";")

df.head()

#%%

#Fazer isso, é a mesma coisa que usar um for

df["qtdePontos"] + 100

#%%

nova_coluna = []


for valores in df['qtdePontos']:
    nova_coluna.append(valores + 100)

nova_coluna

#%%


df["pontos_100"] = df['qtdePontos'] + 100


df.head()

#%%
#É possivel desde que ambas as colunas tenham a mesma dimensão
df['EmailTwitch'] = df['flEmail'] + df['flTwitch']

df.head()

#%%

df['flEmail'] * df['flTwitch']

#%%

df["QtdeSocial"] = df['flEmail'] + df['flTwitch'] + df['flYouTube'] + df['flBlueSky'] + df['flInstagram']


df.head()

#%%

df['Todas_social'] = df['flEmail'] * df['flTwitch'] * df['flYouTube'] * df['flBlueSky'] * df['flInstagram']

df.head()

#%%

df['qtdePontos'].describe()

#%%

df['logPontos'] = np.log(df['qtdePontos'] + 1)

df['logPontos'].describe()

#%%




