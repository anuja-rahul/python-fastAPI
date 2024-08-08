![Python](https://img.shields.io/badge/-python-000?style=for-the-badge&logo=python)
![FAST API](https://img.shields.io/badge/-fast_api-000?style=for-the-badge&logo=fastapi)
![POSTMAN](https://img.shields.io/badge/-postman-000?style=for-the-badge&logo=postman)
![PYDANTIC](https://img.shields.io/badge/-pydantic-000?style=for-the-badge&logo=pydantic)
![POSTGRES](https://img.shields.io/badge/-postgresql-000?style=for-the-badge&logo=postgresql)
![SQLALCHEMY](https://img.shields.io/badge/-sqlalchemy-000?style=for-the-badge&logo=sqlalchemy)
![JWT](https://img.shields.io/badge/-JWT-000?style=for-the-badge&logo=json-web-tokens)

# Python-fastAPI

![GitHub](https://img.shields.io/github/forks/anuja-rahul/python-fastAPI?style&logo=github)
&nbsp;
![GitHub](https://img.shields.io/github/license/anuja-rahul/python-fastAPI?style&logo=github)
&nbsp;
![GitHub](https://img.shields.io/github/stars/anuja-rahul/python-fastAPI?style&logo=github)
&nbsp;
![Contributors](https://img.shields.io/github/contributors/anuja-rahul/python-fastAPI?style&logo=github)
&nbsp;
![Watchers](https://img.shields.io/github/watchers/anuja-rahul/python-fastAPI?style&logo=github)
&nbsp;

[![Project-Status](https://img.shields.io/badge/Project%20Status-adding_query_params-orange.svg)](https://github.com/anuja-rahul/portfolio-nextjs)
&nbsp;

<!--
[![Project-Version](https://img.shields.io/badge/Version-v0.1-green.svg)](https://github.com/anuja-rahul/python-fastAPI)
-->

## Prerequisites  

- [python ≥ 3.10](https://www.python.org/downloads/)
- [postgreSQL ≥ 16.0](https://www.postgresql.org/download/)

## Getting Started  

1. Clone this repository

    ```bash
    git clone https://github.com/anuja-rahul/python-fastAPI.git
    ```

2. Create a Virtual environment

    ```bash
    python -m venv venv
    ```

3. Activate the venv

    ```bash
    activate venv
    ```

4. Install the packages

    ```bash
    pip install -r requirements.txt
    ```

5. Setting up the env variables:  *`required: .env`*  

    ex: *for dev env*

    ```bash
    SECRET_KEY="Your Secret Key"
    ALGORITHM="HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES="60"
    HOST="localhost"
    DBNAME="Your DB name"
    PORT="8000"
    USER="Your Username"
    PASSWORD="Your password"
    ```

    - Note: If you have openssl, to generate a `SECRET_KEY` you can run :
  
        ```bash
        openssl rand -hex 32
        ```

6. Start the uvicorn server

    ```bash
    uvicorn app.main:app --reload
    ```

## Documentation  

- After starting the uvicorn server visit

    for *`Swagger UI`*:

    ```bash
    http://localhost:8000/docs
    ```

    or for *`Redoc`*:

    ```bash
    http://localhost:8000/redoc
    ```

&nbsp;
&nbsp;
&nbsp;

![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=anuja-rahul&repo=python-fastAPI&theme=nightowl)
