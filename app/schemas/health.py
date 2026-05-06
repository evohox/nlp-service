"""
Схемы для эндпоинта /health.
"""

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """Ответ healthcheck'а."""

    status: str = Field(
        default="ok",
        description="Статус сервиса. Всегда 'ok' если сервис отвечает.",
        examples=["ok"],
    )
