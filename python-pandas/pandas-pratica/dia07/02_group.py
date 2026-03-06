#%%

import pandas as pd


# %%


transacoes = pd.read_csv("../arquivos/transacoes.csv", sep=';')

transacoes.head(n=1)
# %%


transacoes.groupby(by=["IdCliente"]).count()
# %%

# agrupa duas colunas, sendo a id cliente o index do total de transacoes

transacoes.groupby(by=["IdCliente"])[["IdTransacao"]].count()

# %%

# as_index=False, faz com que o id_cliente não seja o index

transacoes.groupby(by=["IdCliente"], as_index=False)[["IdTransacao"]].count()
# %%

# Qtde_transações usando agg (agregação)


tot_transacoes = transacoes

tot_transacoes.groupby(by=["IdCliente"],as_index=False).agg( 
    {"IdTransacao":['count'], "QtdePontos": ['sum', 'mean']}
    )

# %%


# Tot_pontos

tot_pontos = transacoes


tot_pontos.groupby(by=["IdCliente"], as_index=False)["QtdePontos"].count()
# %%


# pontos / transacoes

media_pontos = transacoes


media_pontos.groupby(by=["QtdePontos"], as_index=False)["IdTransacao"].mean()
# %%


# Lidando com multiIndex

summary = tot_transacoes.groupby(by=["IdCliente"],as_index=False).agg( 
    {"IdTransacao":['count'], "QtdePontos": ['sum', 'mean']}
    )


summary
# %%

summary[("QtdePontos", "mean")]

# %%


summary.columns = ["IdCliente", "QtdePontos", "TotPontos", "MediaPontos"]

summary
# %%
