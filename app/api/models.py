from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.db.dependencies import get_delete_use_case, get_list_use_case, get_register_use_case
from app.dto.shemas import DeleteResponse, ModelInfo, ModelRegisterRequest
from app.usecase.model_usecase import DeleteModelUseCase, ListModelsUseCase, RegisterModelUseCase

router = APIRouter()

RegisterUseCaseDep = Annotated[RegisterModelUseCase, Depends(get_register_use_case)]
ListUseCaseDep = Annotated[ListModelsUseCase, Depends(get_list_use_case)]
DeleteUseCaseDep = Annotated[DeleteModelUseCase, Depends(get_delete_use_case)]

@router.get("")
async def list_models(use_case: ListUseCaseDep) -> list[ModelInfo]:
    return await use_case.execute()


@router.post("")
async def register_model(
    request: ModelRegisterRequest,
    use_case: RegisterUseCaseDep
) -> ModelInfo:
    try:
        return await use_case.execute(request)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("")
async def delete_model(
    model_name: str,
    use_case: DeleteUseCaseDep
) -> DeleteResponse:
    try:
        return await use_case.execute(model_name)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
