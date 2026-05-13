from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas.books_schema import Book
from app.schemas.responses import Response

from app.services.books_service import load_books, add_book, delete_book


router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/", response_model=List[Book])
def get_books() -> List[Book]:
    return load_books()


@router.get("/{book_id}", response_model=Book)
def get_book(book_id: str) -> Book:
    books = load_books()

    for book in books:
        if book["id"] == book_id:
            return book

    raise HTTPException(status_code=404, detail="Book not found")


@router.get("/{author}", response_model=List[Book])
def get_author_books(author: str) -> List[Book]:
    books = load_books()
    author_books = []

    for book in books:
        if book["author"] == author:
            author_books.append(book)

    raise HTTPException(status_code=404, detail="Author not found")


@router.post("/", response_model=Response)
def added_book(book: Book) -> Response:
    add_book(book)
    return Response(message="Book added successfully")


@router.delete("/{book_id}", response_model=Response)
def del_book(book_id: str) -> Response:
    delete_book(book_id)
    return Response(message="Book deleted successfully")
