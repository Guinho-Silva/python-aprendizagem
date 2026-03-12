#%%

import pandas as pd
# %%

df_geral = pd.read_csv("../arquivos/ipea/homicidios.csv", sep=';')

df_geral = df_geral.rename(columns={"valor": "homicidios"})

df_geral.head()
# %%

df_negros = pd.read_csv("../arquivos/ipea/homicidios-negros.csv", sep=";")

df_negros = df_negros.rename(columns={"valor": "homicidios-negros"})

df_negros.head()
# %%

print(df_geral.columns)
print(df_negros.columns)
#%%

# concatenado pelo index, nome decolunas

df_geral = df_geral.set_index(['nome','período'])

df_negros = df_negros.set_index(['nome','período'])

# %%

# Usando o concatenar

df = pd.concat([df_geral, df_negros], axis='columns')

df
# %%
