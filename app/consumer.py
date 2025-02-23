import asyncio
import json
import time
from collections import deque
from aiokafka import AIOKafkaConsumer
from .db import save_to_db
from .config import KAFKA_BROKER, KAFKA_TOPIC, KAFKA_GROUP_ID

latest_messages = deque(maxlen=10)

async def consume():
    """Читает данные из Kafka и сохраняет в SQLite"""
    while True:  # Бесконечный цикл для автоматического восстановления
        try:
            consumer = AIOKafkaConsumer(
                KAFKA_TOPIC,
                bootstrap_servers=KAFKA_BROKER,
                group_id=KAFKA_GROUP_ID,
                auto_offset_reset="earliest"
            )
            await consumer.start()
            print("✅ Подключено к Kafka, ожидаем сообщения...")

            async for message in consumer:
                try:
                    data = json.loads(message.value)
                    print(f"📥 Получено сообщение: {data}")
                    latest_messages.append(data)

                    if "id" in data:
                        save_to_db(data["id"], json.dumps(data))
                    else:
                        print("⚠ Ошибка: В сообщении нет 'id'")

                except Exception as e:
                    print(f"❌ Ошибка обработки сообщения: {e}")

        except Exception as e:
            print(f"❌ Ошибка Kafka Consumer: {e}. Переподключение через 5 сек...")
            await asyncio.sleep(5)  # Используем `asyncio.sleep` вместо `time.sleep`
        finally:
            await consumer.stop()
