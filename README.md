# Full Stack Project - Product REST API

A REST API built with FastAPI, SQLAlchemy, and PostgreSQL.

## Tech Stack

- **FastAPI** - Web framework
- **SQLAlchemy** - ORM for database operations
- **PostgreSQL** - Database
- **Pydantic** - Data validation

## Project Structure

```
Full_Stack_Project/
└── src/
    ├── main.py       # API routes
    ├── module.py     # SQLAlchemy & Pydantic models
    └── database.py   # Database connection
```

## Setup

1. Install dependencies:
```bash
pip install fastapi sqlalchemy psycopg2-binary uvicorn
```

2. Run the server:
```bash
uvicorn src.main:app --reload
```

3. Open API docs at: `http://127.0.0.1:8000/docs`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/products` | Get all products |
| POST | `/products` | Create a product |
| GET | `/product/{id}` | Get product by ID |
| PUT | `/product/{id}` | Update product by ID |
| DELETE | `/product/{id}` | Delete product by ID |

## Request Body (POST / PUT)

```json
{
  "id": 1,
  "name": "Laptop",
  "price": 999.99,
  "description": "A high-performance laptop"
}
```

## Product Model

| Field | Type |
|-------|------|
| id | int |
| name | str |
| price | float |
| description | str |
