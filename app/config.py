import os
import yaml
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

# Читаем config.yaml
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# База данных (SQLite)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")

# Настройки Kafka
KAFKA_BROKER = os.getenv("KAFKA_BROKER")
KAFKA_TOPIC = config["kafka"]["topic"]
KAFKA_GROUP_ID = config["kafka"]["group_id"]

# Настройки Redis
REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
CACHE_TTL = config["redis"]["cache_ttl"]