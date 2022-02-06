from pydantic import BaseModel


class Recipe(BaseModel):
    id: int
    name: str
    url: str = None

    class Config:
        orm_mode = True
