from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


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
    return Response(respond="Привіт з сервера2")
