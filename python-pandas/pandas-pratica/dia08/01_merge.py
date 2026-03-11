#%%

import pandas as pd
# %%

clientes = pd.read_csv("../arquivos/clientes.csv", sep=';')

clientes.head(n=2)

#%%

transacoes = pd.read_csv("../arquivos/transacoes.csv", sep=';')

transacoes.head(n=2)
# %%

transacoes.head()

# %%
# Equivale a o  join como se fosse o left join
transacoes.merge(right=clientes, how="left", left_on="IdCliente",right_on="idCliente", suffixes=["Transacao", "Cliente"])

# %%


#Exemplo de quando o id é diferente

df_1 = pd.DataFrame({
    "Transacao": [1,2,3,4,5],
    "idCliente" : [1,2,3,4,5],
    "valor": [10,45,32,17,85],
})


df_2 = pd.DataFrame({
    "id": [1,2,3,4],
    "Nome": ["Iago", "Teo", "Nah", "Jose"],
})

df_2
#%%

df_1.merge(df_2, left_on="idCliente", right_on="id", how="left")
# %%

# fazer filtro (pegar apenas colunas especificas)

# var[[nome colunas]]

# df = df[df["colunaReferencia"]== coluna]