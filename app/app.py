from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

text_posts = {
    1: {"title": "Primeiro Post", "content": "Olá, este é o início do meu blog em Python!"},
    2: {"title": "Dica de Ubuntu", "content": "Sempre use 'sudo apt update' antes de instalar pacotes."},
    3: {"title": "DevOps Life", "content": "Automação não é sobre ferramentas, é sobre cultura."},
    4: {"title": "FastAPI é rápido?", "content": "Sim, a performance de IO assíncrono é impressionante."},
    5: {"title": "Debugando venv", "content": "Lembre-se de verificar se o interpretador no VS Code é o da .venv."},
    6: {"title": "Configuração de Rede", "content": "Testando o failover entre dois provedores de internet."},
    7: {"title": "Cloudflare API", "content": "Automatizando registros DNS via script Python."},
    8: {"title": "Docker 101", "content": "Containers facilitam a vida de quem desenvolve no Linux."},
    9: {"title": "Clean Code", "content": "Escreva código para humanos, não apenas para máquinas."},
    10: {"title": "Deploy Final", "content": "Subindo a aplicação para produção com Uvicorn e Gunicorn."}
}

@app.get("/posts")
def get_all_posts(limit: int = None) -> list[PostResponse]:
    if limit:
        if limit > len(text_posts):
            raise HTTPException(status_code=400, detail="limit exceeds total number of posts")
        
        if limit <= 0:
            raise HTTPException(status_code=400, detail="limit must be a positive integer")
        
        return list(text_posts.values())[:limit]

    return list(text_posts.values())

@app.get("/posts/{id}")
def get_one_post(id: int)-> PostResponse:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="post not found")
    
    return text_posts.get(id)

@app.post("/posts")
def create_post(post: PostCreate) -> PostResponse:
    new_post= {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post
