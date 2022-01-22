from operator import index
from sqlalchemy import Column, Integer, String
from .database import Base


class Recipe(Base):
    __tablename__ = "Recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)