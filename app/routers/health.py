"""
Роутер для healthcheck-эндпоинта.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
async def healthcheck() -> dict[str, str]:
    """
    Простейший healthcheck.
    Возвращает {"status": "ok"} с кодом 200.
    """
    return {"status": "ok"}
