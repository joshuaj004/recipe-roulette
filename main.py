from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/recipes/{recipe_id}")
def read_recipe(recipe_id: int):
    return {"recipe_id": recipe_id}

@app.post("/recipes/")
def create_recipe(recipe_name: str):
    return {"recipe_id": recipe_name}