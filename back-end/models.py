from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from database import Base
import json

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    filmesFavoritos = Column(String)
    artistasFavoritos = Column(String)

    def get_favorites(self):
        return json.loads(self.filmesFavoritos) if self.filmesFavoritos else []

    def set_favorites(self, favorites):
        self.filmesFavoritos = json.dumps(favorites)

    def get_favorite_artists(self):
        return json.loads(self.artistasFavoritos) if self.artistasFavoritos else []

    def set_favorite_artists(self, favorite_artists):
        self.artistasFavoritos = json.dumps(favorite_artists)