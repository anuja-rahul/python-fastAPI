from typing import List, Optional
from ..database import get_db
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import Response, status, HTTPException, Depends, APIRouter

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)


# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), 
              limit: int = 10, offset: int = 0, search: Optional[str] = ""):
    # cursor.execute("""
    #     SELECT * FROM posts""")
    # posts = cursor.fetchall()
    # print(posts)x
    # print(limit)

    posts = db.query(models.Post).filter(
        models.Post.title.contains(search)).order_by(models.Post.created_at).limit(limit).offset(offset).all()
    # posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()

    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()

    # print(results)
    # return posts
    return results


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""
    #     INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""", 
    #     (post.title, post.content, post.published))
    # new_post = cursor.fetchone()
    # conn.commit()

    # print(post)
    # print(post.model_dump())
    # post_dict = post.model_dump()
    # post_dict['id'] = randrange(0, 1000000)
    # my_posts.append(post_dict)

    # new_post = models.Post(title=post.title, content=post.content, published=post.published)
    # print(current_user.id)

    new_post = models.Post(owner_id=current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, response: Response, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""
    #     SELECT * FROM posts WHERE id = %s """, ((str(id)), ))
    # test_post = cursor.fetchone()
    # print(test_post)
    # post = find_post(id)

    post = db.query(models.Post).filter(models.Post.id == id).first()
    
    if not post:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return{"data": f"post with id: {id} was not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorized to perform this action")
    return post


# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p
        

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
        

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""
    #                DELETE FROM posts WHERE id = %s RETURNING *""", ((str(id)), ))
    # deleted_post = cursor.fetchone()
    # conn.commit()

    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()   


    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorized to perform this action")
    
    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), 
                current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""
    #                UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", 
    #                (post.title, post.content, post.published, (str(id))))
    # updated_post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You are not authorized to perform this action")
    
    # post_dict = post.model_dump()
    # post_dict["id"] = id
    # my_posts[index] = post_dict

    post_query.update(updated_post.model_dump(), synchronize_session=False)
    db.commit()

    return post_query.first()
