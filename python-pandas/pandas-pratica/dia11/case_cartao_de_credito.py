#%%

import pandas as pd
# %%

df = pd.read_csv('case_cartao.csv', sep=';')

df
#%%

# Converte a coluna para data 

df['dtTransacao'] = pd.to_datetime(df['dtTransacao'])

df

# %%

df['vlParcela'] = df['vlVenda'] / df['qtdeParcelas']

df

# %%

df['ordemParcela'] = df.apply( lambda row: [i for i in range(row['qtdeParcelas'])], axis=1)

df
# %%

df_explodio = df.explode('ordemParcela')

df_explodio
# %%


# df_explodio["dtParcela"]= df_explodio.apply(lambda row: row['dtTransacao'] + pd.DateOffset(months=row['ordemParcela']), axis=1)

# df_explodio
# %%


def calcDtParcela(row):
    dt = row["dtTransacao"] + pd.DateOffset(months=row["ordemParcela"])

    dt = f'{dt.year} - {dt.month}'

    return dt

df_explodio['dtParcela'] = df_explodio.apply(calcDtParcela, axis=1)

df_explodio

#%%

(
    df_explodio.groupby(['idCliente', 'dtParcela'])
    ['vlParcela'].sum()
    .reset_index()
    .pivot_table(index='idCliente',columns='dtParcela',values='vlParcela',fill_value=0)
)
# %%
