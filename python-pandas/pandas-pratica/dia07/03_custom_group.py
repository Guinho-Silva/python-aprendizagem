#%%

import pandas as pd

import numpy as np
# %%

transacoes = pd.read_csv("../arquivos/transacoes.csv",sep=';')

transacoes.head(n=2)


#%%


def diff_amp(x:pd.Series):
    amplitude = x.max() - x.min()

    media = x.mean()

    return np.sqrt((amplitude - media)**2)

def life_time(x:pd.Series):
    dt = pd.to_datetime(x)

    return (dt.max() - dt.min()).days



idades = pd.Series([23, 34, 32, 12, 54, 65, 64, 25, 45,])

diff_amp(idades)
# %%

transacoes.groupby(by=["IdCliente"]).agg({
    "IdTransacao": ['count'],
    "QtdePontos": ['sum', 'mean', diff_amp],
    "DtCriacao": [life_time]
})



# %%

transacoes.columns

# %%
