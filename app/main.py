from typing import Optional, Tuple, List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from . import schemas

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs/")

@app.get("/recipes/", response_model=List[schemas.Recipe])
def read_all_recipes(db: Session = Depends(get_db)):
    record = db.query(models.Recipe).all()
    return record


@app.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
def read_recipe(db: Session = Depends(get_db), recipe_id: int = None):
    record = db.query(models.Recipe).get(recipe_id)
    return record

@app.post("/recipes/")
def create_recipe(recipe_name: str, db: Session = Depends(get_db)):
    db_record = models.Recipe(
        name = recipe_name
    )
    db.add(db_record)
    db.commit()
    return {"recipe_id": db_record.id}