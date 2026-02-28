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

    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y").dt.date

    exp1= st.expander("Dados Brutos")

    # Exibição dos dados no App

    columns_fat = {"Valor": st.column_config.NumberColumn("Valor", format="R$%d")}

    exp1.dataframe(df, hide_index=True, column_config = columns_fat)

    #Visão instituição
    exp2 = st.expander("Instituições")

    df_instituicao = df.pivot_table(index="Data", columns = "Instituição", values="Valor")

    tab_data, tab_history, tab_share = exp2.tabs(["Dados", "Histórico", "Distribuição"])


    with tab_data:

        st.dataframe(df_instituicao)

    #Gráfico
    with tab_history:
        st.line_chart(df_instituicao)

    with tab_share:

        date = st.date_input("Data para Distribuição", min_value=df_instituicao.index.min(),
        max_value=df_instituicao.index.max())

        if date not in df_instituicao.index:
            st.warning("Entre com uma data válida")
        
        else:
            #Obtem a ultima data de dados
            last_dt =  df_instituicao.sort_index().iloc[-1]

            st.bar_chart(last_dt)