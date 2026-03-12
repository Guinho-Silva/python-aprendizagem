# %%

import pandas as pd
#%%
df = pd.DataFrame({
    "Cliente": [1,2,3,4,5],
    "nome": ["Iago", "Teo", "Jose", "Nah", "Kozato"]
})


df_02 = pd.DataFrame({
    "Cliente": [6,7,8],
    "nome": ["Laura", "Dan", "Lah"],
    "idade": [32,29,31]
})

df_03 = pd.DataFrame({

    "Idade": [32,34,19,54,33]
})
# %%

# Para usar o concat, ele espera que usemos uma lista

# dfs = [df, df_02]

pd.concat([df, df_02], ignore_index=True)
# %%
# depois de reordenar os valores, devemos resetar os indicies

df_03 = df_03.sort_values(by="Idade").reset_index(drop=True)

df_03
# %%

pd.concat([df, df_03], ignore_index=True)

#%%
# Eu posso definir como eu quero concatenar



pd.concat([df, df_03], axis='columns')

# usando o 'Columns' eu concateno como coluna


# %%

# Case ipea