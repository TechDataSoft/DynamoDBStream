import redis
import json
from .config import REDIS_HOST, REDIS_PORT, CACHE_TTL

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def cache_record(record_id, data):
    """Кеширует данные в Redis"""
    redis_client.setex(record_id, CACHE_TTL, json.dumps(data))

def get_cached_record(record_id):
    """Получает данные из кеша"""
    data = redis_client.get(record_id)
    return json.loads(data) if data else None
