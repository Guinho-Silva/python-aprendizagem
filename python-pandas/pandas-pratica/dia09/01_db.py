#%%
import pandas as pd

import sqlalchemy

#%%

# %%

engine = sqlalchemy.create_engine("sqlite:///../arquivos/olist.db")

# %%


clientes = pd.read_sql_table(table_name="tb_customers", con=engine)
# %%

clientes.shape
# %%

# Faça uma query par anão puxar todos os dados

query = "SELECT * FROM tb_customers LIMIT 50"

df_100 = pd.read_sql_query(query, con=engine)

df_100
# %%
