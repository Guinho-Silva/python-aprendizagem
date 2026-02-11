#%%

import pandas as pd

DataFrame = pd.read_csv("../arquivos/transacoes.csv", sep=';')

DataFrame.head(n=2)
#%%
# Filtrar por MAIOR usando FOR

pontos = [10, 1,2, 3, 5, 67, 345, 1, 1, 3, 25, 50]

valores_50_mais = []

for num in pontos:
    if num >= 50:
        valores_50_mais.append(num)

valores_50_mais

#%%
#Segunda forma de Fazer
valores_50_mais = [num for num in pontos if num >=50]

valores_50_mais

#Carimbando os valores

pontos = [10, 1,2, 3, 5, 67, 345, 1, 1, 3, 25, 50]

filtro_carimbo = []

for num in pontos:
   filtro_carimbo.append(num>=50)

resultado = []
for num in(range(len(pontos))):
    if pontos[num]:
        resultado.append(pontos[num])

resultado
#%%

pontos = [10, 1,2, 3, 5, 67, 345, 1, 1, 3, 25, 50]

filtro= []

valores_50_mais = []

for i in pontos:
    filtro.append(i>=50)

resultado = []

for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])
resultado
# %%

#Usando o Pandas

#Cria um dataframe de 3 linhas
brinquedo = pd. DataFrame( {
        "nome": ["teo", "nah", "mah"],
        "idade": [32,35,14],
        "uf": ["sp", "pr", "rj"],     
     })

brinquedo.index = brinquedo.index + 1

#variaavel responsavél pela a verificação do operado lógico, retornando uma serie boleana
filtro_serie = brinquedo["idade"] >= 18


#Atribui a serie filtro para a variavel brinquedo, com a verificação logica
brinquedo[filtro_serie]
#%%

#Usando a verificação lógica no dataset para retornar valores maior ou igual a 50

DataFrame = pd.read_csv("../arquivos/transacoes.csv", sep=';')

DataFrame.head(n=2)

Maior_50_Pontos = DataFrame["QtdePontos"] >=50

DataFrame[Maior_50_Pontos].head(n=3)

#%%
#Usando a verificação lógica no dataset para retornar valores maior ou igual a 50 e menor que 100

DataFrame = pd.read_csv("../arquivos/transacoes.csv", sep=';')

DataFrame.head(n=2)

Maior_50_e_100_pontos = (DataFrame["QtdePontos"]>=50) & (DataFrame["QtdePontos"] < 100)

DataFrame[Maior_50_e_100_pontos]

#%%

#Usando o filtro or

DataFrame = pd.read_csv("../arquivos/transacoes.csv", sep=';')

DataFrame.head(n=2)

filtro = (DataFrame["QtdePontos"] == 1) | (DataFrame["QtdePontos"] > 100) 

DataFrame[filtro]

#%%
#Usando os operadores e/ou para retornar dois dados distintos
DataFrame = pd.read_csv("../arquivos/transacoes.csv", sep=';')

DataFrame.head(n=2)

filtro2 = (DataFrame['QtdePontos'] > 0) & (DataFrame['QtdePontos'] <= 50) | (DataFrame['DtCriacao'] >= '2025-01=01')

DataFrame[filtro2]