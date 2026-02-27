import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finanças",page_icon="")

st.text("Olá, Mundo")


st.markdown("""
# Boas vindas

## Nosso APP Finanaceiro
            
Espero que você curta a experiência da nossa solução para organização financeira.

""")

file_upload = st.file_uploader(label="Faça o upload do arquivo aqui", type=["csv"])

# Verifica se algum algum arquivo teve upload
if file_upload:

    #leitura dos dados
    df = pd.read_csv(file_upload)

    # Exibição dos dados no App

    columns_fat = {"Valor": st.column_config.NumberColumn("Valor", format="R$%d")}

    st.dataframe(df, hide_index=True, column_config = columns_fat)