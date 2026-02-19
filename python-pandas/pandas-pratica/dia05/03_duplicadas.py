#%%

import pandas as pd

#%%

df = pd.DataFrame({
        "nome": ["Teo", "Iago", "Marcio", "Nah", "Bia", "Iago", "Iago"],

        "Sobrenome": ["Calvo", "Silva", "Calvo", "Silva", "Ataido", "Silva", "Silva"]
    }
)

df

#%%


#Ele removerá o utimo registro duplicado

df.drop_duplicates()

#%%


#Manterá o ultimo registro
df.drop_duplicates(keep="last") 

#%%


brinquedo = pd.DataFrame(
    {
        "nome": ["Teo", "Iago", "Marcio", "Nah", "Bia", "Iago", "Iago"],

        "Sobrenome": ["Calvo", "Silva", "Calvo", "Silva", "Ataido", "Silva", "Silva"],
        "salario": [3453, 4532, 3456, 5432, 5457, 1349, 4643]
    }
)

brinquedo

#%%
#Organiza a coluna salario do mai para o men

brinquedo =brinquedo.sort_values("salario", ascending=False)

brinquedo
#%%
#Remove duas linhas de colunas especificadas

brinquedo.drop_duplicates(keep= 'last', subset=["nome", "Sobrenome"])