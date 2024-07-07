from typing import Optional
from fastapi import FastAPI, Response
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [{"title": "title of post 1", "content": "Content of post 1", "id": 1}, {"title": "title of post 2", "content": "Content of post 2", "id": 2}]


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
    post_dict = post.model_dump()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return{"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        response.status_code = 404
    return{"data": post}


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
