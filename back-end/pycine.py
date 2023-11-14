import asyncio
from typing import List
from fastapi import FastAPI, HTTPException, Depends, Response
from tmdb import get_json
from sqlalchemy import update
from schemas import Item
from sqlalchemy.orm import Session
import crud, models

app = FastAPI()

from fastapi.middleware.cors import (
     CORSMiddleware
)
# habilita CORS (permite que o Svelte acesse o fastapi)
origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

# =====================================================
# USERS
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 3 ENDPOINTS
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.put("/users/{item_id}", response_model=schemas.Item)
def update_user(item_id: str, item: Item):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


# ========================================================

# ATIVIDADE 1

@app.get("/filme/{title}")
async def find_movie(title: str):
    """ 
    procura filmes pelo titulo e ordena pelos mais populares 
    Exemplo: /filme/avatar
    """
    return {"title": title}

# ========================================================

# ATIVIDADE 2

@app.get("/artista/filmes")
async def find_filmes_artista(personId: int):
    """ 
    busca os filmes mais populares de um artista 
    Exemplo: /artista/filmes?personId=1100
    """
    return {"id": personId}

# ========================================================

@app.get("/filmes")
async def filmes_populares(limit=3):
    data = get_json("discover/movie", "&sort_by=vote_count.desc")

    results = data['results']

    filtro = []

    for movie in results[:5]:
        filtro.append({
            "title": movie['original_title'],
            "image": f"http://image.tmdb.org/t/p/w500{movie['poster_path']}",
            "id": movie['id']
        })
    
    return filtro

@app.get("/artistas/{name}")
async def get_artista(name: str):
    """ 
    obtem lista de artista pelo nome e popularidade 
    """
    data = get_json(
        "/search/person", f"?query={name}&language=en-US"
    )
    results = data['results']
    filtro = []
    for artist in results:
        filtro.append({
            'id': artist['id'],
            'name': artist['name'],
            'rank': artist['popularity']
        })
    # ordenar lista de artistas (filtro) pelo atributo rank
    filtro.sort(reverse=True, key=lambda artist:artist['rank'])
    # return data
    return filtro


@app.get("/artista/{id}")
async def get_artista(id):
    data = get_json(
        f"person/{id}",""
    )

    return data

@app.post("/favoritos/{user_id}/{filme_id}")
async def salvar_favorito(user_id: int, filme_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    favoritos = crud.get_favorites(db, user_id)

    if favoritos is None:
        favoritos = []
    
    if filme_id in favoritos:
        return {"message": "Filme já está na lista de favoritos."}

    crud.add_favorite(db, user_id, filme_id)

    return {"message": "Filme adicionado aos favoritos com sucesso."}

@app.delete("/favoritos/{user_id}/{filme_id}")
async def excluir_favorito(user_id: int, filme_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if crud.remove_favorite(db, user_id, filme_id) is not None:
        return Response(status_code=204)
    else:
        raise HTTPException(status_code=404, detail="Favorite not found")

@app.get("/favoritos/{user_id}")
async def get_favoritos(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    ids = crud.get_favorites(db, user_id)

    favoritos = []

    for id in ids:
        filme = get_json(f"movie/{id}","")
        favoritos.append({
            "id": filme['id'],
            "title": filme['original_title'],
            "image": f"http://image.tmdb.org/t/p/w500{filme['poster_path']}",
        })

    return favoritos