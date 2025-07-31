from fastapi import FastAPI, HTTPException, UploadFile, File, Depends, status, APIRouter
from .dependencies import get_manager
from ..core.DB import init_db
from ..models.Base import ModelInfo, ModelRegisterRequest, DeleteResponse
from ..models.manager import ModelManager

# Инициализация БД
init_db()

router = APIRouter()


@router.post("/models/register")
async def register_model(
        request: ModelRegisterRequest,
        manager: ModelManager = Depends(get_manager)
):
    try:
        return manager.register_model(request)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


@router.post("/predict/{model_name}")
async def predict():
    pass


@router.get("/models")
async def list_models(manager: ModelManager = Depends(get_manager)):
    return manager.get_models_list()


@router.delete("/models/{model_name}")
async def delete_model(
        model_name: str,
        manager: ModelManager = Depends(get_manager)
):
    try:
        manager.unload_model(model_name)
        # В реальной реализации нужно удалять из БД через репозиторий
        return DeleteResponse(
            status="success",
            message=f"Модель {model_name} удалена"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )


@router.get("/status")
async def health_check():
    return {}