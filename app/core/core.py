from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from app.core.DB import AIModel
from app.models.manager import ModelManager

class ModelRepository:
    """Класс для работы с базой данных моделей"""
    def __init__(self, db: Session):
        self.db = db

    def get_model(self, name: str) -> type[AIModel] | None:
        return self.db.query(AIModel).filter(AIModel.name == name).first()

    def get_all_models(self) -> list[type[AIModel]]:
        return self.db.query(AIModel).all()

    def create_model(self, name: str, config: Dict) -> AIModel:
        db_model = AIModel(name=name, config=config)
        self.db.add(db_model)
        self.db.commit()
        self.db.refresh(db_model)
        return db_model

    def delete_model(self, name: str) -> bool:
        model = self.get_model(name)
        if model:
            self.db.delete(model)
            self.db.commit()
            return True
        return False

