import json
from typing import List
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


# Завдання 4
# Напишіть сервер для симуляції роботи бібліотеки.
# Дані про книги знаходяться у файлі books.json
# Напишіть модель на pydentic для книги з такими
# даними:
# ● id
# ● title
# ● author
# ● year
# ● pages
# Функціонал:
# 1. Отримання всіх книг
# ○ шлях – books
# ○ метод – GET
# 2. Отримання даних за ID книги
# ○ шлях – books/{book_id}
# ○ метод – GET
# 3. Додавання нової книги
# ○ шлях – books
# ○ метод – POST
# 4. Видалення книги за ID
# ○ шлях – books/{book_id}
# ○ метод – DELETE


class Book(BaseModel):
    id: str
    title: str
    author: str
    year: int
    pages: int


@app.get("/books")
def get_books() -> List[Book]:
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("File not found")
        return []


@app.get("/books/{book_id}")
def get_book(book_id: str):
    try:
        with open("books.json", "r", encoding="utf-8") as file:
            books = json.load(file)

            for book in books:
                if book["id"] == book_id:
                    return book

    except FileNotFoundError:
        print("File not found")
        return {}


@app.post("/books")
def save_book(book: Book) -> Message:
    with open("books.json", "r", encoding="utf-8") as file:
        books = json.load(file)

    books.append(book.model_dump())

    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file)

    return Message(message="Book added successfully")


@app.delete("/books/{book_id}")
def delete_book(book_id: str) -> Message:
    with open("books.json", "r", encoding="utf-8") as file:
        books = json.load(file)
        new_books = [b for b in books if b["id"] != book_id]

    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(new_books, file)

    return Message(message="Book deleted successfully")
