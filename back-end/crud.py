import json
from sqlalchemy.orm import Session
import models, schemas

def get_user(db: Session, user_id: int):
    # SELECT * from users where id = user_id
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_favorites(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    return json.loads(user.filmesFavoritos) if user and user.filmesFavoritos else []

def add_favorite(db: Session, user_id:int, movie_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    favoritos = get_favorites(db, user.id)

    if movie_id not in favoritos:
        favoritos.append(movie_id)

    user.filmesFavoritos = json.dumps(favoritos)
    db.commit()
    db.refresh(user)

    return user

def remove_favorite(db: Session, user_id:int, movie_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    favoritos = get_favorites(db, user.id)

    favoritos = [id for id in favoritos if id != movie_id]

    user.filmesFavoritos = json.dumps(favoritos)
    db.commit()
    db.refresh(user)

    return user

def get_favorite_artists(db: Session, user_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    return json.loads(user.artistasFavoritos) if user and user.artistasFavoritos else []

def add_favorite_artist(db: Session, user_id: int, artist_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    favorite_artists = get_favorite_artists(db, user.id)

    if artist_id not in favorite_artists:
        favorite_artists.append(artist_id)

    user.artistasFavoritos = json.dumps(favorite_artists)
    db.commit()
    db.refresh(user)

    return user

def remove_favorite_artist(db: Session, user_id: int, artist_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()

    favorite_artists = get_favorite_artists(db, user.id)

    favorite_artists = [id for id in favorite_artists if id != artist_id]

    user.artistasFavoritos = json.dumps(favorite_artists)
    db.commit()
    db.refresh(user)

    return user