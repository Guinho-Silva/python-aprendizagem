#%%

import pandas as pd

import requests


# %%

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

# Simula um navegador real
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

response = requests.get(url, headers=headers)
df = pd.read_html(response.text)


# %%


uf = df[1]

uf
# %%

numero = "251 529,2"

def str_to_float(x:str):

    x = float(x.replace(" ", "").replace(",",".").replace("\xa0", ""))
    
    return x
# %%

uf.head()
# %%

#Alterando os tipos das colunas

uf["Área (km²)"]

#%%
uf["Área (km²)"]= uf["Área (km²)"].apply(str_to_float)

#%%

uf["População (Censo 2022)"]=uf["População (Censo 2022)"].apply(str_to_float)

uf

#%%

uf["PIB (2015)"]=uf["PIB (2015)"].apply(str_to_float)

# %%



uf["PIB per capita (R$) (2015)"]=uf["PIB per capita (R$) (2015)"].apply(str_to_float)

#%%

"População (Censo 2022)", "Densidade (2005)", "PIB (2015)", "(% total) (2015)", "PIB per capita (R$) (2015)"

#%%

x = "73,9 anos"

float(x.replace(",", ".").replace(" anos", "")
)

# %%
def exp_to_anos(x):
    x= float(x.replace(",", ".").replace(" anos", "")
    )
    return x
#%%

uf["Expectativa de vida (2016)"].apply(exp_to_anos)

# %%
uf.head(2)


#%%
#Como usar o apply em um dataframe
#%%



#%%
#Atividade pegar a alfabetização e mudar, e mortalidade infantil