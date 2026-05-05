from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

# Завдання 1
# Напишіть сервер:
# ● шлях – /hello
# ● метод – POST
# Функція має повертати JSON об’єкт
# {"message": "Привіт з сервера!"}
# Запустіть сервер:
# ● host – localhost
# ● port – 8000
# uvicorn main:app --port 8000 –host localhost --reload
# Напишіть клієнта який робить запит на сервер


class Message(BaseModel):
    message: str


# @app.post("/hello")
# def start() -> Message:
#     return Message(
#         message="Привіт з сервера!",
#     )


# Завдання 2
# Напишіть сервер1:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8000
# Напишіть сервер2:
# ● шлях – /greeting
# ● метод – GET
# ● результат – {"respond": "Привіт з сервера1"}
# ● порт – 8001
# Запустіть обида сервери на localhost
# Напишіть клієнта який робить запита на обидва
# сервери


class Response(BaseModel):
    respond: str


@app.get("/greeting")
def greet() -> Response:
    return Response(respond="Привіт з сервера1")


# Завдання 3
# Напишіть сервер з такими функціями
# ● hello
# ○ шлях – /hello/{name}
# ○ метод – POST
# ○ повертає {"message": "Привіт, {ім'я}!"}
# ● hello_json
# ○ шлях – /hello_json
# ○ метод – POST
# ○ повертає {"message": "Привіт, {ім'я}!"}
# Для hello_json напишіть модель за допомогою
# pydantic
# Запустіть сервер
# Напишіть клієнта який робить запити на сервер


class User(BaseModel):
    name: str


@app.post("/hello")
def save_message(name: str) -> Message:
    return Message(message=f"привіт, {name}")
