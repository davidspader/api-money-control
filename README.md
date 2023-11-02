# API - Expenses control

**FastAPI, PostgreSQL, SQLAlchemy, Alembic, JWT, Pytest**

## Dependecies

* Docker
* Docker-compse
* Poetry

## How to run

Add the environment variables in the `.env` file.

Start **project containers**

```shell
docker-compose up -d
```

Start environment

```shell
poetry shell
```

Install python dependencies

```shell
poetry install
```

Run **alembic** migrations

```shell
docker-compose run app sh -c "alembic upgrade head"
```

Run tests

```shell
docker-compose run app sh -c "pytest"
```

- The application will run at: **http://localhost:8000**
- You can see the API documentation at: **http://localhost:8000/docs**
- The PGAdmin will run at: **http://localhost:5050**
