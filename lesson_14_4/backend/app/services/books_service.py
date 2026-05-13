import json
from pathlib import Path
from fastapi import HTTPException
from typing import List, Dict

from settings_backend.settings_app import settings
from app.schemas.books_schema import Book


BOOKS_FILE = Path(settings.data_file_path)


def load_books() -> List[Dict[str, str | int]]:
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Books file not found.")
        return []


def save_books(books: List[Dict]) -> None:
    try:
        with open(BOOKS_FILE, "w", encoding="utf-8") as file:
            json.dump(books, file, indent=2)

    except FileNotFoundError:
        print("Books file not found.")


def add_book(book: Book) -> None:
    books = load_books()

    if len(books) == settings.max_books:
        raise HTTPException(
            status_code=409, detail=f"Maximum number of books is {settings.max_books}"
        )

    books.append(book.model_dump())
    save_books(books)


def delete_book(book_id: str) -> None:
    books = load_books()
    new_books = [book for book in books if book["id"] != book_id]
    save_books(new_books)
