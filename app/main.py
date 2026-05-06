"""
Точка входа в приложение.
"""

from fastapi import FastAPI

from app.routers import health

app = FastAPI(
    title="NLP Service",
    description="REST API для классификации текстов, NER и извлечения IoC.",
    version="0.1.0",
)

# Подключаем роутер healthcheck'а к основному приложению.
app.include_router(health.router)
