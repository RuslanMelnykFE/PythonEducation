from fastapi import APIRouter, HTTPException

from app.schemas.films_schema import Movie
from app.schemas.responses import Response


from app.services.films_service import (
    load_movies,
    add_movie,
    delete_movie,
)


router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/{movie_id}", response_model=Movie)
def get_movie(movie_id: str) -> Movie:
    movies = load_movies()

    for movie in movies:
        if movie["id"] == movie_id:
            return movie

    raise HTTPException(status_code=404, detail="Movie not found")


@router.post("/", response_model=Response)
def added_movie(movie: Movie) -> Response:
    add_movie(movie)
    return Response(message="Movie added")


@router.delete("/{movie_id}", response_model=Response)
def del_movie(movie_id: str):
    delete_movie(movie_id)
    return Response(message="Movie deleted")
