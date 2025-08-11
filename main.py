import uvicorn
from sqlalchemy.orm import Session
from uvicorn import logging
from app.api import status, predict, models
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import settings
from app.db.database import init_db, engine

app = FastAPI()

app.include_router(status.router)
app.include_router(predict.router)
app.include_router(models.router)

logger = logging.getLogger("uvicorn")

@asynccontextmanager
async def lifespan():
    logger.info("Starting application")
    logger.info("Initializing database")
    await init_db()
    logger.info(f"Using database: {settings.database_url}")
    logger.info("Application startup complete")

    yield

    # Очистка при остановке
    logger.info("Shutting down application...")
    logger.info("Closing database connections...")
    await engine.dispose()
    logger.info("Application shutdown complete")


if __name__ == "__main__":
    uvicorn.run(app)