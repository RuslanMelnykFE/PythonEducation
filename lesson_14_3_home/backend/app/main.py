import uvicorn

from fastapi import FastAPI
from app.routers.films_route import router as films


app = FastAPI()
app.include_router(films)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8080,
        reload=True,
    )
