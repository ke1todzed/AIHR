from app.db.database import AIModel
from app.dto.shemas import DeleteResponse, ModelInfo, ModelRegisterRequest
from app.service.manager import ModelManager


class RegisterModelUseCase:
    def __init__(self, service: ModelManager) -> None:
        self.service = service

    async def execute(self, request: ModelRegisterRequest) -> ModelInfo:
        return await self.service.register_model(request)


class ListModelsUseCase:
    def __init__(self, service: ModelManager) -> None:
        self.service = service

    async def execute(self) -> list[ModelInfo]:
        return await self.service.get_models_list()


class DeleteModelUseCase:
    def __init__(self, service: ModelManager) -> None:
        self.service = service

    async def execute(self, model_name: str) -> DeleteResponse:
        # Удаление из БД
        model = await self.service.session.get(AIModel, model_name)
        if not model:
            raise ValueError(f"Model {model_name} not found")

        await self.service.session.delete(model)
        await self.service.session.commit()

        # Выгрузка из памяти (если была загружена)
        await self.service.unload_model(model_name)

        return DeleteResponse(
            status="success",
            message=f"Model {model_name} deleted"
        )
