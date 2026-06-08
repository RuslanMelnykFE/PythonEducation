import dotenv
import os

dotenv.load_dotenv()


class Config:
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    USER = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    DB = os.getenv("DB")

    DB_URI = f"postgresql+pg8000://{USER}:{PASSWORD}@{HOST}/{DB}"
