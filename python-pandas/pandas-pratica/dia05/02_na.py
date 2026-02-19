#%% 

import pandas as pd

clientes = pd.read_csv("../arquivos/clientes.csv", sep= ';')

clientes.head(30)

#%%
#Exclui qualquer NaN


clientes.dropna(how='all')#só limpará se a linha inteira for vazia

clientes.dropna(how='any')#limpará tudo
#%%

brinquedo = pd.DataFrame(
    {
        "nome": ["Teo", None, "Nah", "Marcio"],

        "idade": [None, None, "43", "52"],

        "salario": [3453, 4532, None, 5432]
    }
)

brinquedo.dropna(how='all', subset=["idade", "nome"])
#%%
brinquedo.dropna(how='any', subset=["idade", "salario", "nome"])

#%%

#Fillna irá prencher os valores nulos

brinquedo["idade"].fillna(0)


brinquedo.fillna({"nome": 'Iago', "idade": 20})
#%%

media = brinquedo[["idade", "salario"]]. mean()

brinquedo.fillna(media)
