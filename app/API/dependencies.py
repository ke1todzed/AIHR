from fastapi import Depends
from sqlalchemy.orm import Session
from ..core.DB import get_db
from ..core.core import ModelRepository
from ..models.manager import ModelManager


def get_repository(db: Session = Depends(get_db)) -> ModelRepository:
    return ModelRepository(db)

def get_manager(repo: ModelRepository = Depends(get_repository)) -> ModelManager:
    return ModelManager(repo)