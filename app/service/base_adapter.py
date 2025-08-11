from abc import abstractmethod
from pydantic import BaseModel
from typing import Any, Dict

class BaseAdapter(BaseModel):
    @abstractmethod
    async def predict(self, input_data: Any) -> Any:
        pass

    @abstractmethod
    async def preprocess(self, raw_input: Dict[str, Any]) -> Any:
        pass

    @abstractmethod
    async def postprocess(self, model_output: Any) -> Dict[str, Any]:
        pass