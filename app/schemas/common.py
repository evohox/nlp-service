"""
Общие Pydantic-схемы, которые переиспользуются между разными эндпоинтами.
"""

from pydantic import BaseModel, Field


class TextRequest(BaseModel):
    """
    Базовая схема для запросов, принимающих один текст.
    """

    text: str = Field(
        ...,
        min_length=1,
        max_length=10_000,
        description="Входной текст для обработки.",
        examples=["Hello, world!"],
    )
