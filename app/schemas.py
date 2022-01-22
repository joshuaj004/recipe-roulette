from pydantic import BaseModel

class Recipe(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True