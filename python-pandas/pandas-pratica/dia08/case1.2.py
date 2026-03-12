#%%
import pandas as pd

import os 
# %%

# Criando a função para tratar arquivos de um unico conjunto de dados

def le_arquivos(nome_arquivo):
    df = (pd.read_csv(f"../arquivos/ipea/{nome_arquivo}.csv", sep=';')
              .rename(columns={"valor":nome_arquivo})
              .set_index(["nome", "período"])
              .drop(["cod"],axis='columns')
        )
    return df

#%%

nome_arquivos = os.listdir("../arquivos/ipea/")

nome_arquivos
# %%

dfs = []

for arquivos in  nome_arquivos:
    nome_arquivos = arquivos.split(".")[0]
    dfs.append(le_arquivos(nome_arquivos))
# %%

df_full = (pd.concat(dfs,axis='columns')
    .reset_index()
    .sort_values(["período","nome"]))

df_full

# df_full.to_csv("homicidios_consolidado.csv", index=False,sep=';')
# %%
