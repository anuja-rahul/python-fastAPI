from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


@app.get("/")
def root():
    return{"message": "Hello World."}

@app.get("/posts")
def get_posts():
    return{"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    print(post)
    print(post.model_dump())
    return{"data": "data received"}


my_posts = [{"title": "title of post 1", "content": "Content of post 1", "id": 1}, {"title": "title of post 2", "content": "Content of post 2", "id": 2}]
