from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()

@router.post("")
async def predict():
    pass
