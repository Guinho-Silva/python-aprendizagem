#%%

import pandas as pd

clientes = pd.read_csv("../arquivos/clientes.csv", sep= ';')


# sort_values ordena 

clientes['qtdePontos'].sort_values()

#%%

max_pontos = clientes['qtdePontos'].max()

clientes[clientes['qtdePontos']==max_pontos]

#%%

# Assim ele ordena o dataFrame, mas eu preciso infomaar pelo oq eu vou ordenar
clientes.sort_values(by="qtdePontos", ascending=False).head(n=5)

# Ele não esta alternando o dataFrame, ele esta CRIANDO um novo

#%%

brinquedo = pd.DataFrame(
    {
        "nome": ["teo", "ana", "nah", "jose"],
        "idade": [32, 43, 35, 42],
        "salario":[2345, 4533, 3245, 4533]
    }
)

brinquedo

#%%

#Ele primeiro ira ordena pelo salario e dps pela idade, o mesmo vale para o ascending
brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])