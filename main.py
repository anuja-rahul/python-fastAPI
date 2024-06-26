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
    return{"Data": "This is your posts."}

@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    print(new_post.model_dump())
    return{"data": "data received"}

