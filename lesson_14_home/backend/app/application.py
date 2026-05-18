from fastapi import FastAPI
from app.routers.films_route import router as films


app = FastAPI()
app.include_router(films)
