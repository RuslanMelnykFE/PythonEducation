from pydantic import BaseModel


class Movie(BaseModel):
    id: str
    title: str
    director: str
    year: int
