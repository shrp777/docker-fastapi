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


class TaskEntity(Base):
    """
    Modèle de la table tasks
    """
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String, nullable=False)
    urgence = Column(Integer, sa.CheckConstraint(
        'urgence > 0 AND urgence < 6'), nullable=False)
    importance = Column(Integer, sa.CheckConstraint(
        'importance > 0 AND importance < 6'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.utcnow)
    is_completed = Column(Boolean, default=False, nullable=False)
    completed_at = Column(DateTime, nullable=True)


class Task(BaseModel):
    """
    Task avec id + created_at + updated_at + completed_at
    """
    id: Optional[int] = None
    content: str
    urgence: int
    importance: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    is_completed: Optional[bool] = False

    class Config:
        from_attributes = True


# class TaskCreateDTO(TaskBase):
#     """
#     Task sans id (utile pour la création)
#     """
#     pass


Base.metadata.create_all(engine)
