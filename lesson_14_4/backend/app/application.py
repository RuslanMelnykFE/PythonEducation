from fastapi import FastAPI
from app.routers.books_route import router as books


app = FastAPI()
app.include_router(books)
