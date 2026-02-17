# Smart Task Manager

A full-stack Task Management system built with FastAPI (backend) and Streamlit (UI).
This project demonstrates REST API design, database integration, CRUD operations, filtering logic, and frontend-backend communication.

---

## Tech Stack

Backend:

* FastAPI
* SQLAlchemy ORM
* SQLite
* Pydantic v2

Frontend:

* Streamlit
* Requests

Utilities:

* Faker (for fake data seeding)

---

## Features

* Create, Update, Delete tasks
* Toggle task completion
* Search by title
* Filter by priority
* Filter by completion status
* Fake data generation script
* Clean project structure (UI separated from backend)

---

## Project Structure

```
├── UI
│   └── main.py        # Streamlit frontend
├── database.py        # Database configuration
├── fake.py            # Fake data generator
├── main.py            # FastAPI backend
├── models.py          # SQLAlchemy models
├── schemas.py         # Pydantic schemas
├── requirements.txt
└── tasks.db
```

---

## Installation

Clone the repository and install dependencies:

```
pip install -r requirements.txt
```

---

## Run Backend

Start FastAPI server:

```
uvicorn main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

API Documentation available at:

```
http://127.0.0.1:8000/docs
```

---

## Seed Fake Data

To populate the database with demo tasks:

```
python fake.py
```

---

## Run Frontend (Streamlit UI)

```
streamlit run UI/main.py
```

Frontend runs at:

```
http://localhost:8501
```

---

## API Endpoints

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| POST   | /tasks/     | Create task     |
| GET    | /tasks/     | List all tasks  |
| GET    | /tasks/{id} | Get single task |
| PUT    | /tasks/{id} | Update task     |
| DELETE | /tasks/{id} | Delete task     |

---

## What This Project Demonstrates

* RESTful API design
* Clean backend architecture
* Pydantic v2 schema handling
* SQLAlchemy ORM usage
* State management in Streamlit
* Frontend filtering logic
* Database session handling best practices

---
