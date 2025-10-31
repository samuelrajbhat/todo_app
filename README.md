# Todo App with FastAPI

A Todo application built with FastAPI, SQLAlchemy, and JWT authentication.  
Users can register, log in, and manage personal todo items securely.

---

## Features

- User registration and login with JWT
- CRUD operations for todo items
- Protected routes for authenticated users
- Passwords hashed with Passlib & Bcrypt
- Pydantic models for request validation

---

## Tech Stack

- Python 3.11, FastAPI, SQLAlchemy, PostgreSQL (or SQLite)
- Passlib & Bcrypt, Pydantic

---

## Installation

1. Clone the repo:
git clone https://github.com/yourusername/todo-app.git
cd todo-app


2. Create & activate virtual environment:

python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Run the app:

uvicorn main:app --reload