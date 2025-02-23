import json
from aiokafka import AIOKafkaProducer
import asyncio
from app.config import KAFKA_BROKER, KAFKA_TOPIC

producer = None  # Глобальный объект продюсера

async def get_producer():
    """Возвращает единственный экземпляр Kafka-продюсера"""
    global producer
    if producer is None:
        producer = AIOKafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        await producer.start()
    return producer

async def send_data(record):
    """Отправляет данные в Kafka"""
    producer = await get_producer()
    try:
        await producer.send_and_wait(KAFKA_TOPIC, record)
        print("✅ Данные отправлены в Kafka:", record)
    except Exception as e:
        print(f"❌ Ошибка отправки в Kafka: {e}")

async def close_producer():
    """Останавливает продюсера при завершении работы"""
    global producer
    if producer:
        await producer.stop()
        producer = None

if __name__ == "__main__":
    async def main():
        sample_data = {"id": "123", "name": "Test Record", "value": 42}
        await send_data(sample_data)
        await close_producer()  # Закрываем соединение после теста

    asyncio.run(main())