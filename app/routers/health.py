"""
Роутер для healthcheck-эндпоинта.
"""

from fastapi import APIRouter

from app.schemas.health import HealthResponse

router = APIRouter(prefix="/health", tags=["health"])


@router.get("", response_model=HealthResponse)
async def healthcheck() -> HealthResponse:
    """
    Простейший healthcheck.
    Возвращает {"status": "ok"} с кодом 200.
    """
    return HealthResponse(status="ok")
