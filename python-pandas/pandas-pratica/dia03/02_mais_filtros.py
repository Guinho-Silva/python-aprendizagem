#%%

import pandas as pd

DataFrame = pd.read_csv("../arquivos/transacao_produto.csv", sep=';')

DataFrame

#%%

Filtro1 = (DataFrame["IdProduto"] == 5) | (DataFrame["IdProduto"] == 11)


DataFrame[Filtro1]

# %%

Filtro1= DataFrame['IdProduto'].isin([5,11])

DataFrame[Filtro1]
#%%

clientes = pd.read_csv("../arquivos/clientes.csv", sep=';')

clientes.head()


filtro = clientes['DtCriacao'].notna()

clientes[filtro]
#%%
# Negando
~clientes['DtCriacao'].isna()

clientes['DtCriacao'].notna()

