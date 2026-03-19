#%%
import pandas as pd

# %%


df = pd.read_csv("../arquivos/ipea/homicidios_consolidado.csv", sep=';')

df.head()
# %%

df_stack = (df.set_index(["nome", "período"]).stack().reset_index())

df_stack.columns = ["nome", "período", "metrica", "valor"]

df_stack
# %%

(df_stack.pivot_table(values='valor', index=["nome", "período"], columns="metrica").reset_index())
