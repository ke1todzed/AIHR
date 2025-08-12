from __future__ import annotations

from fastapi import APIRouter

router = APIRouter()

@router.get("")
async def health_check():
    return "OK"
