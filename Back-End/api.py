
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
