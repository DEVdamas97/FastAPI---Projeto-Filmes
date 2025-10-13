import streamlit as st

# Rodar o streamlit
# python -m streamlit run app.py

import requests 

# Criar minha rota de api
# URL da api do FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="(☞ﾟヮﾟ)☞ 🎬 ", page_icon="🍿")

st.title(" Gerenciador de Filmes")

# Menu lateral sidebar

menu = st.sidebar.radio("Navegação", ["Catalogo"])

if menu == "Catalogo":
    st.subheader("Todos os Filmes 📽")
    respose = requests.get(f"{API_URL}/filmes")
    if respose.status_code == 200:
        filmes = respose.json().get("filmes", [])
        if filmes:
            for filme in filmes:
                st.write(
                    f"🎬 **{filme['titulo']}** "
                    f"({filme['ano']})  \n"
                    f"📌 Gênero: {filme['genero']}  \n"
                    f"⭐ Avaliação: {filme.get('avaliacao', 'N/A')}"
                )
    else:
        st.error("Erro ao cone")
