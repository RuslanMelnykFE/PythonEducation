# # Напишіть клієнта з таким фуннкціоналом для
# # користувача:
# # ● отримати дані про фільм
# # ● додати новий фільм
# # ● видалити фільм


import requests


URL = "http://0.0.0.0:8080"


def get_movie(movie_id: str) -> dict[str, str | int]:
    response = requests.get(f"{URL}/movies/{movie_id}")
    print(f"Get movie: {response}")
    return response.json()


def add_movie() -> None:
    movie = {"id": "uty", "title": "Hello", "director": "Jon", "year": 2026}
    response = requests.post(f"{URL}/movies", json=movie)
    print(f"Add movie: {response}")


def delete_movie(movie_id: str) -> None:
    response = requests.delete(f"{URL}/movies/{movie_id}")
    print(f"Delete movie: {response}")


add_movie()
get_movie("uty")
delete_movie("uty")
