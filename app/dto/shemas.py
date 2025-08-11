from pydantic import BaseModel
from typing import Dict, Any, Optional


class ModelConfig(BaseModel):
    path: str
    model_type: str
    parameters: Dict[str, Any]

class ModelRegisterRequest(BaseModel):
    name: str
    config: ModelConfig

class ModelInfo(BaseModel):
    id: int
    name: str
    path: str
    model_type: str
    parameters: Dict[str, Any]
    is_loaded: bool
    load_count: int
    last_used: Optional[str]

class PredictionRequest(BaseModel):
    input_data: Dict[str, Any]

class PredictionResponse(BaseModel):
    model: str
    prediction: Any
    status: str
    config: Dict[str, Any]

class DeleteResponse(BaseModel):
    status: str
    message: str