import uvicorn
from settings_backend.settings_app import settings


if __name__ == "__main__":
    uvicorn.run(
        "app.application:app",
        host=settings.host,
        port=settings.port,
        reload=True,
    )
