import streamlit as st
import scipy.stats
import time
import pandas as pd

st.header('Jogando uma moeda')

# Cria um gráfico de linhas vazio com um valor inicial de 0.5
chart = st.line_chart([0.5])

def toss_coin(n):
    # Simula n lançamentos de moeda com probabilidade 0.5 (Bernoulli)
    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)
    
    mean = None
    outcome_no = 0
    outcome_1_count = 0
    
    # Loop para calcular a média a cada novo lançamento e atualizar o gráfico
    for r in trial_outcomes:
        outcome_no += 1
        if r == 1:
            outcome_1_count += 1
        mean = outcome_1_count / outcome_no
        
        # Adiciona a nova média ao gráfico existente
        chart.add_rows([mean])
        
        # Pequena pausa para criar o efeito de animação
        time.sleep(0.05)
        
    return mean

number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)
start_button = st.button('Executar')

if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas...')
    # Chama a função e inicia a animação
    final_mean = toss_coin(number_of_trials)
    st.write(f'Média final: {final_mean:.4f}')