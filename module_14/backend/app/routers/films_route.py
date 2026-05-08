from fastapi import APIRouter, HTTPException

from typing import List

from module_14.backend.app.models.films_model import Movie
from module_14.backend.app.models.responses import Response

from module_14.backend.app.services.films_service import (
    load_movies,
    add_movie,
    delete_movie,
)


router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("/{movie_id}", response_model=List[Movie])
def get_movie(movie_id: str) -> dict[str, str | int] | None:
    movies = load_movies()

    for movie in movies:
        if movie["id"] == movie_id:
            return movie
        else:
            raise HTTPException(status_code=404, detail="Movie not found")

    return None


@router.post("/", response_model=Response)
def added_movie(movie: Movie) -> Response:
    add_movie(movie)
    return Response(message="Movie added")


@router.delete("/movies/{movie_id}")
def del_movie(movie_id: str):
    delete_movie(movie_id)
