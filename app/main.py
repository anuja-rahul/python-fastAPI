from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange
import psycopg
import time
# from psycopg.rows import dict_row

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    

while True:
    try:
        conn = psycopg.connect(host = "localhost", dbname="fastapi", user="fastapiuser", password="password123")
        cursor = conn.cursor(row_factory=psycopg.rows.dict_row)
        print("\nDatabase connection was successfull !\n")
        break

    except Exception as error:
        print("\nConnecting to databse failed ! :", error)
        time.sleep(2)


my_posts = [{"title": "title of post 1", "content": "Content of post 1", "id": 1}, {"title": "title of post 2", "content": "Content of post 2", "id": 2}]


@app.get("/")
def root():
    return{"message": "Hello World."}


@app.get("/posts")
def get_posts():
    cursor.execute("""
        SELECT * FROM posts""")
    posts = cursor.fetchall()
    print(posts)
    return{"data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cursor.execute("""
        INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", 
        (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    # print(post)
    # print(post.model_dump())
    # post_dict = post.model_dump()
    # post_dict['id'] = randrange(0, 1000000)
    # my_posts.append(post_dict)
    return{"data": new_post}


@app.get("/posts/{id}")
def get_post(id: int, response: Response):
    cursor.execute("""
        SELECT * FROM posts WHERE id = %s """, ((str(id)), ))
    test_post = cursor.fetchone()
    print(test_post)
    # post = find_post(id)
    if not test_post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{"data": f"post with id: {id} was not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return{"data": test_post}


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p
        

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i
        

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""
                   DELETE FROM posts WHERE id = %s RETURNING *""", ((str(id)), ))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""
                   UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", 
                   (post.title, post.content, post.published, (str(id))))
    updated_post = cursor.fetchone()
    conn.commit()
    

    if updated_post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    # post_dict = post.model_dump()
    # post_dict["id"] = id
    # my_posts[index] = post_dict

    return{"data": updated_post}