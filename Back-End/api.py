
from fastapi import FastAPI

import funcao


# Deve entrar na pasta
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


@app.put("/filmes/{id_filme}")
def atualizar_filme(id_filme: int, nova_avaliacao: float):
    funcao.atualizar_movies(id_filme, nova_avaliacao)
    filme = funcao.buscar_movies()
    if filme:
        funcao.atualizar_movies(id_filme, nova_avaliacao)
        return {"mensagem": "filme atualizado com sucesso!"}
    return {"erro": "Filme não encontrado"}

@app.delete("/filme")
def deletar(id_filme:int):
    funcao.deletar_filme(id_filme)
    deletar = funcao.deletar_filme()
    if deletar:
        funcao.deletar(id_filme)
        return {"mensagem": "filme deletado com sucesso"}