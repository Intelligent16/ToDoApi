from datetime import datetime

from fastapi import FastAPI, Response
from starlette import status

from data_base import todos
from model import Todo
from to_do_service import find_by_id, get_and_increment_id

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/name/{name}")
async def root(name):
    return {"message": "Hello " + name}


@app.get("/todo")
async def todo():
    return {"message": todos}


@app.get("/todo/{id}")
async def get_todo(id: int, response: Response):
    todo = find_by_id(id)
    if todo is None:
        response.status_code = status.HTTP_404_NOT_FOUND  # для отображения на фронте
        return
    return {"todo": todo}


@app.post("/todo")
async def add_todo(todo: Todo):
    todo.id = get_and_increment_id()
    todo.creationDate = datetime.now()
    todos.append(todo)
    return todo
