
from fastapi import FastAPI

import funcao

# Rodar o fast api = python -m uvicorn api:app --reload

# Para testar as rotas no fastapi

# /docs > socumentação Swagger

# /reload > Documentação Redoc

app = FastAPI(title="Gerenciador de Filmes")

# GET > Pegar/Listar
# POST > Enviar/Cadastrar
# PUT > Atualizar
# Delete > Deletar


# API sempre retorna dados em JSON (chave:valor)
@app.get("/")
def home():
    return {
        "mensagem": "Bem-Vindo ao gerenciador de filmes!"
    }


@app.get("/filmes")
def catalogo():
    filmes = funcao.listar_movies()
    lista = []
    for linha in filmes:
        lista.append({
            "id": linha[0],
            "titulo": linha[1],
            "genero": linha[2],
            "ano": linha[3],
            "avaliacao": linha[4]
        })
    return {
        "filmes": lista
    }


@app.post("/filmes")
def adicionar_filme(titulo: str, genero: str, ano: int, avaliacao: float):
    funcao.criar_filme(titulo, genero, ano, avaliacao)
    return {"mensagem": "Filme adicionado com sucesso"}