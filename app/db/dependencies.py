from __future__ import annotations

from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.service.manager import ModelManager
from app.usecase.model_usecase import DeleteModelUseCase, ListModelsUseCase, RegisterModelUseCase

AsyncSessionDep = Annotated[AsyncSession, Depends(get_db)]

async def get_service(
    session: AsyncSessionDep
) -> AsyncGenerator[ModelManager, None]:
    yield ModelManager(session)

async def get_register_use_case(
    service: ModelManager = Depends(get_service)
) -> RegisterModelUseCase:
    return RegisterModelUseCase(service)

async def get_list_use_case(
    service: ModelManager = Depends(get_service)
) -> ListModelsUseCase:
    return ListModelsUseCase(service)

async def get_delete_use_case(
    service: ModelManager = Depends(get_service)
) -> DeleteModelUseCase:
    return DeleteModelUseCase(service)
