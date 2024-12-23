import os
import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Boolean, func

from pydantic import BaseModel

from datetime import datetime

from typing import Optional


DB_URL = os.getenv('DATABASE_URL')

engine = create_engine(
    DB_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Ci-dessous, la définition du modèle de données avec l'ORM SQLAlchemy génère automatiquement la table dans la base de données


class PizzaEntity(Base):
    """
    Modèle de la table pizzas géré par l'ORM SQLAlchemy
    - valeur de created_at est automatiquement initialisée à la création d'un item
    - valeur de updated_at est automatiquement initialisée à la mise à jour d'un item
    """
    __tablename__ = "pizzas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.utcnow)


class Pizza(BaseModel):
    """
    Modèle de données Pydantic
    """
    id: Optional[int] = None
    name: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


Base.metadata.create_all(engine)
