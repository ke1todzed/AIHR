from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.db.database import AIModel
from app.dto.shemas import ModelRegisterRequest, ModelInfo

class ModelManager:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def register_model(self, request: ModelRegisterRequest) -> ModelInfo:
        # Проверка существования модели
        existing_model = await self.session.execute(
            select(AIModel).where(AIModel.name == request.name))
        if existing_model.scalars().first():
            raise ValueError(f"Model {request.name} already exists")

        # Создание новой модели
        new_model = AIModel(
            name=request.name,
            path=request.config.path,
            model_type=request.config.model_type,
            parameters=request.config.parameters
        )

        self.session.add(new_model)
        await self.session.commit()
        await self.session.refresh(new_model)

        return self._convert_to_dto(new_model)

    async def get_models_list(self) -> list[ModelInfo]:
        result = await self.session.execute(select(AIModel))
        models = result.scalars().all()
        return [self._convert_to_dto(model) for model in models]

    async def unload_model(self, name: str) -> bool:
        model = await self.session.get(AIModel, name)
        if not model:
            return False

        # Выгрузка модели
        model.is_loaded = False
        await self.session.commit()
        return True

    def _convert_to_dto(self, model: AIModel) -> ModelInfo:
        return ModelInfo(
            id=model.id,
            name=model.name,
            path=model.path,
            model_type=model.model_type,
            parameters=model.parameters,
            is_loaded=model.is_loaded,
            load_count=model.load_count,
            last_used=model.last_used.isoformat() if model.last_used else None
        )


