import streamlit as st

# Título do App
st.header('Jogando uma moeda')

# Widget 1: Controle deslizante (Slider)
# Parâmetros: Rótulo, Valor Mínimo, Valor Máximo, Valor Padrão
number_of_trials = st.slider('Número de tentativas?', 1, 1000, 10)

# Widget 2: Botão
start_button = st.button('Executar')

# Lógica que acontece quando o botão é clicado
if start_button:
    st.write(f'Executando o experimento de {number_of_trials} tentativas...')
    
# Mensagem de rodapé
st.write('Ainda não é um aplicativo funcional. Em construção.')