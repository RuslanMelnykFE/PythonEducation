from fastapi import FastAPI
from module_14.backend.app.routers.films_route import router as films


app = FastAPI()
app.include_router(films)
