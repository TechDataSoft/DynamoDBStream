from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import get_record
from app.cache import get_cached_record
from app.producer import send_data
from app.consumer import consume, latest_messages
import asyncio

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Фоновый запуск Kafka Consumer при старте API"""
    task = asyncio.create_task(consume())  # Запускаем Consumer в фоне
    try:
        yield  # Запуск API
    finally:
        task.cancel()  # Остановить Consumer
        try:
            await task  # Дождаться остановки
        except asyncio.CancelledError:
            pass  # Ожидаем завершения, игнорируем исключение


app = FastAPI(lifespan=lifespan)

@app.get("/record/{record_id}")
async def get_data(record_id: str):
    """Получает запись по ID"""
    data = get_cached_record(record_id)
    if not data:
        data = get_record(record_id)
    return data

@app.post("/send/")
async def send_kafka_message(message: dict):
    """Отправляет сообщение в Kafka"""
    await send_data(message)
    return {"status": "Сообщение отправлено", "message": message}

@app.get("/latest-messages")
async def get_latest_messages():
    """Возвращает последние 10 сообщений из Kafka"""
    return list(latest_messages)
