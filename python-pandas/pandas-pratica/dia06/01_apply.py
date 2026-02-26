#%%

import pandas as pd

# %%

#Importa o arquivo

df = pd.read_csv("../arquivos/clientes.csv",sep=';')

df.head()


# %%

idCliente = '000dc0f6-e4f2-4a42-b8cd-b586ed1c709a'


#O split é um separador de strings

idCliente.split('-')[-1]


# %%

def get_last_id(x):
    return x.split('-')[-1]


# %%

get_last_id('000dc0f6-e4f2-4a42-b8cd-b586ed1c709a')

# %%


#Criando uma nova coluna com o seumo dos clientes

id_novo= []

for valor in df['idCliente']:
    novo_id = get_last_id(valor)
    id_novo.append(novo_id)


df["novo_id"] = id_novo
df.head()

# %%

#Aplicando uma função
df["idCliente"].apply(get_last_id)

# %%
