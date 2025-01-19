import streamlit as st

# Título do aplicativo
st.title("MVP de Vitivinicultura")

# Entrada de dados do usuário
st.sidebar.header("Parâmetros de Consulta")
opcao = st.sidebar.selectbox(
    "Escolha uma categoria:",
    ["Produção", "Processamento", "Comercialização", "Importação", "Exportação"]
)

# Exibição dos resultados
st.write(f"Você selecionou a categoria: **{opcao}**")

st.write("Esta é uma demonstração de um MVP utilizando Streamlit!")
