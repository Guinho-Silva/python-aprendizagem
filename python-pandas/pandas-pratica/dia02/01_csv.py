
#%%
import pandas as pd

#Aqui lê o arquivo
df = pd.read_csv("../arquivos/clientes.csv",sep=";")

df

#%%

#Salva o arquivo sem indicies
df.to_csv("clientes.csv", index=False)

df = pd.read_csv("clientes.csv")

df
#%%

# Lê arquivo parquet
df.to_parquet("clientes.parquet", index=False)

df_2 = pd.read_parquet("clientes.parquet")

#%%

df.to_excel("clientes.xlsx", index=False)

#%%

df_3 = pd.read_excel("clientes.xlsx")

df_3