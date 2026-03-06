#%%

import pandas as pd
# %%

idades = [34, 45, 53, 34, 32, 54, 67, 12, 43, 44, 52, 14, 15, 45, 87, 67]

idades = pd.Series(idades)

idades
# %%

idades.sum()
# %%

idades.min()

# %%

idades.max()

# %%

idades.mean()
# %%

idades.describe()
# %%

clientes = pd.read_csv("../arquivos/clientes.csv", sep=';')

clientes.head(n=2)
# %%

clientes["flTwitch"].sum()

clientes['flTwitch'].mean()
# %%


redes_sociais = ['flEmail', 'flTwitch',	'flYouTube', 'flBlueSky', 'flInstagram']

clientes[redes_sociais].mean()
# %%

filtro = clientes.dtypes == "object"

#%%

num_columns= clientes.dtypes[~filtro].index.tolist()
num_columns
clientes[num_columns].mean()
# %%

clientes.dtypes
# %%
#Retorna um data frame

clientes[num_columns].describe()

# %%
 

# %%
