from fastapi import FastAPI
import psycopg
import time
from . import models
from .database import engine
from .routers import post, user
# from pydantic import BaseModel
# from passlib.context import CryptContext
# from random import randrange
# from psycopg.rows import dict_row
# from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg.connect(host = "localhost", dbname="fastapi", user="fastapiuser", password="password123")
        cursor = conn.cursor(row_factory=psycopg.rows.dict_row)
        print("\nDatabase connection was successfull !\n")
        break

    except Exception as error:
        print("\nConnecting to databse failed ! :", error)
        time.sleep(2)


# my_posts = [{"title": "title of post 1", "content": "Content of post 1", "id": 1}, {"title": "title of post 2", "content": "Content of post 2", "id": 2}]


app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
def root():
    return{"message": "Hello World."}


# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"data": posts}






