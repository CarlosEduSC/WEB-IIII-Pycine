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
    favoritos = Column(String)

    def get_favorites(self):
        return json.loads(self.favoritos) if self.favoritos else []

    def set_favorites(self, favorites):
        self.favoritos = json.dumps(favorites)