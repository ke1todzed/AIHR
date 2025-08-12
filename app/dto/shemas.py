from __future__ import annotations

from typing import Any

from pydantic import BaseModel


class ModelConfig(BaseModel):
    path: str
    model_type: str
    parameters: dict[str, Any]

class ModelRegisterRequest(BaseModel):
    name: str
    config: ModelConfig

class ModelInfo(BaseModel):
    id: int
    name: str
    path: str
    model_type: str
    parameters: dict[str, Any]
    is_loaded: bool
    load_count: int
    last_used: str | None

class PredictionRequest(BaseModel):
    input_data: dict[str, Any]

class PredictionResponse(BaseModel):
    model: str
    prediction: Any
    status: str
    config: dict[str, Any]

class DeleteResponse(BaseModel):
    status: str
    message: str
