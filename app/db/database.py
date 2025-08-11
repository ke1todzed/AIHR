from datetime import datetime
from typing import Any, AsyncGenerator, Dict, Optional
from sqlalchemy import Integer, String, JSON, Boolean, DateTime
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column
from app.db.config import settings

Base = declarative_base()


class AIModel(Base):
    __tablename__ = 'models'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    path: Mapped[str] = mapped_column(String(255), nullable=False)
    model_type: Mapped[str] = mapped_column(String(50), nullable=False)
    parameters: Mapped[Dict[str, Any]] = mapped_column(JSON, nullable=False)
    is_loaded: Mapped[bool] = mapped_column(Boolean, default=False)
    load_count: Mapped[int] = mapped_column(Integer, default=0)
    last_used: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


engine = create_async_engine(settings.database_url,future=True,echo=settings.debug,pool_pre_ping=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=False)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db() -> AsyncGenerator:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()