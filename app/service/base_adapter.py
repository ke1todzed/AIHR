from abc import abstractmethod
from typing import Any

from pydantic import BaseModel


class BaseAdapter(BaseModel):
    @abstractmethod
    async def predict(self, input_data: Any) -> Any:
        pass

    @abstractmethod
    async def preprocess(self, raw_input: dict[str, Any]) -> Any:
        pass

    @abstractmethod
    async def postprocess(self, model_output: Any) -> dict[str, Any]:
        pass
