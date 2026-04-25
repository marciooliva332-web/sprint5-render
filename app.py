import streamlit as st
import pandas as pd
import plotly_express as px

# 1. Ler os dados
df = pd.read_csv('vehicles.csv')

# 2. Cabeçalho do Aplicativo
st.header('Análise de Inventário de Veículos')

# 3. Checkboxes para os gráficos
build_histogram = st.checkbox('Criar histograma')
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_histogram:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(df, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, width="stretch")

if build_scatter:
    st.write('Criando um gráfico de dispersão para o preço vs. odômetro')

    # criar gráfico de dispersão
    fig_scatter = px.scatter(df, x="odometer", y="price")

    # exibir gráfico
    st.plotly_chart(fig_scatter, width="stretch")