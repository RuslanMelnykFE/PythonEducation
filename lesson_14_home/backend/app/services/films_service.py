import json
from pathlib import Path
from typing import List, Dict
from fastapi import HTTPException

from settings_app import settings
from app.schemas.films_schema import Movie


MOVIES_FILE = Path(settings.data_file_path)


def load_movies() -> List[Dict[str, str | int]]:
    try:
        with open(MOVIES_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Movies file not found.")
        return []


def save_movies(movies: List[Dict]) -> None:
    try:
        with open(MOVIES_FILE, "w", encoding="utf-8") as file:
            json.dump(movies, file, indent=2)

    except FileNotFoundError:
        print("Movies file not found.")


def add_movie(movie: Movie) -> None:
    movies = load_movies()

    if len(movies) == settings.max_films:
        raise HTTPException(
            status_code=409, detail=f"Maximum number of films is {settings.max_films}"
        )

    movies.append(movie.model_dump())
    save_movies(movies)


def delete_movie(movie_id: str) -> None:
    movies = load_movies()
    new_movies = [movie for movie in movies if movie["id"] != movie_id]
    save_movies(new_movies)
