from abc import ABC
from typing import List, Dict, Optional, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.core.DB import AIModel
from app.core.core import ModelRepository
from app.models.Base import ModelRegisterRequest, ModelInfo
from base_adapter import BaseAdapter
import json
from typing import List, Dict, Any
from pydantic import BaseModel
from sqlalchemy.orm import Session




class ModelManager:
    def __init__(self, repository: ModelRepository):
        self.repo = repository
        self.loaded_models: Dict[str, Any] = {}

    def register_model(self, request: ModelRegisterRequest) -> ModelInfo:
        if self.repo.get_model(request.name):
            raise ValueError(f"Model {request.name} already exists")

        db_model = self.repo.create_model(
            name=request.name,
            config=request.config.model_dump()
        )

        self.loaded_models[request.name] = {
            'config': request.config.model_dump(),
            'instance': None  # Здесь будет загруженная модель
        }

        return ModelInfo(
            id=db_model.id,
            name=db_model.name,
            config=db_model.config
        )

    def get_models_list(self) -> List[ModelInfo]:
        return [
            ModelInfo(
                id=model.id,
                name=model.name,
                config=model.config
            )
            for model in self.repo.get_all_models()
        ]

    def unload_model(self, name: str) -> bool:
        if name in self.loaded_models:
            del self.loaded_models[name]
            return True
        return False
