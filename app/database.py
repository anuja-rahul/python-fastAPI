from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# from dotenv import load_dotenv
# import os

# import psycopg
# import time
# from pydantic import BaseModel
# from passlib.context import CryptContext
# from random import randrange
# from psycopg.rows import dict_row
# from sqlalchemy.orm import Session
# from dotenv import load_dotenv
# import os


# load_dotenv()

# HOST = os.getenv("HOST")
# DBNAME = os.getenv("DBNAME")
# USER = os.getenv("USER")
# PASSWORD = os.getenv("PASSWORD")


# while True:
#     try:
#         conn = psycopg.connect(host=HOST, dbname=DBNAME, user=USER, password=PASSWORD)
#         cursor = conn.cursor(row_factory=psycopg.rows.dict_row)
#         print("\nDatabase connection was successfull !\n")
#         break

#     except Exception as error:
#         print("\nConnecting to databse failed ! :", error)
#         time.sleep(2)

# my_posts = [{"title": "title of post 1", "content": "Content of post 1", "id": 1}, {"title": "title of post 2", "content": "Content of post 2", "id": 2}]


# load_dotenv()

# SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
# SQLALCHEMY_DATABASE_URL = "postgresql://username:password@hostname:port/db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.USER}:{settings.PASSWORD}@{settings.HOST}:{settings.PORT}/{settings.DBNAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()