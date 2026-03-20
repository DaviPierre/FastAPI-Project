from fastapi import FastAPI, HTTPException

app = FastAPI()

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
def get_all_posts():
    return text_posts

@app.get("/posts/{id}")
def get_one_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="post not found")
    
    return text_posts.get(id)
