import pandas as pd
import streamlit as st
import plotly_express as px

# Lendo os dados
df = pd.read_csv('vehicles.csv')

# Título do App
st.header('Análise de Dados de Veículos')

# Criando um botão para exibir a tabela
if st.checkbox('Mostrar tabela de dados'):
    st.write(df)

# Criando um histograma com Plotly
st.subheader('Distribuição do Ano dos Modelos')
fig = px.histogram(df, x="model_year")
st.plotly_chart(fig)