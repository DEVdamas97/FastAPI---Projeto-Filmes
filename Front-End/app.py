import streamlit as st
import requests
# Rodar o streamlit
# python -m streamlit run app.py

import requests 

# Criar minha rota de api
# URL da api do FastAPI

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="(☞ﾟヮﾟ)☞ 🎬 ", page_icon="🍿")

st.title(" Gerenciador de Filmes")

# Menu lateral sidebar

menu = st.sidebar.radio("Navegação", ["Catalogo", "Adicionar Filme", "Atualizar Filme"])

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
                st.info("Nenhum filme cadastrado")
    else:
        st.error("Erro ao conectar")
elif menu == "Adicionar Filme":
     st.subheader("➕  Adicionar Filme")

     titulo = st.text_input("Digite o Titulo do filme: ")
     genero = st.text_input("Digite o genero do filme: ")
     ano = st.number_input("Digite o ano de lançamento: ", min_value=1900, max_value = 2050, step=1)
     avaliacao = st.number_input("Digite a avaliação (1 a 10)", min_value=0, max_value=10, step=1)

     if st.button("Salvar Filme 📂"):
          params =  {
               "titulo": titulo,
               "genero": genero,
               "ano": ano,
               "avaliacao": avaliacao
               }
          respose = requests.post(f"{API_URL}/filmes", params=params)
          if respose.status_code == 200:
               st.success("Filme Adicionado com Sucesso!")
          else:
               st.error("Erro ao Adicionar o Filme")

elif menu == "Atualizar Filme":
    st.subheader("Atualizar dados de um Filme 📁")

    id_filme = st.number_input("ID do filme que deseja atualizar", min_value=1, step=1)
    nova_avaliacao = st.number_input("Nova Avaliação", min_value=1, max_value=10)
    if st.button("Atualizar"):
        dados = {"nova_avaliacao": nova_avaliacao}
        response = requests.put(f"{API_URL}/filmes/{id_filme}", params=dados)
        if response.status_code == 200:
            data = response.json()
            if "error" in data:
                st.warning(data["erro"])
            else:
                 st.success("Filme atualizado com sucesso")
        else:
             st.error("Erro ao atualizar o filme")