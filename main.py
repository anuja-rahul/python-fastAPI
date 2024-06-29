from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def root():
    return{"message": "Hello World."}


@app.get("/posts")
def get_posts():
    return{"Data": "This is your posts."}


@app.post("/createposts")
def create_posts(new_post: Post):
    print(new_post)
    return{"data": "data received"}

