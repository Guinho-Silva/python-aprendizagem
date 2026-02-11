#%%

import pandas as pd

DataFrame = pd.read_csv("../arquivos/transacao_produto.csv", sep=';')

DataFrame

#%%

Filtro1 = (DataFrame["IdProduto"] == 5) | (DataFrame["IdProduto"] == 11)


DataFrame[Filtro1]
