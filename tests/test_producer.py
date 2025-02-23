import json
import pytest
from unittest.mock import patch, MagicMock
from app.producer import send_data


@pytest.fixture
def mock_kafka_producer():
    """Создаем mock KafkaProducer"""
    with patch("app.producer.KafkaProducer") as MockProducer:
        mock_producer = MagicMock()
        MockProducer.return_value = mock_producer
        yield mock_producer


def test_send_data(mock_kafka_producer):
    """Тестируем отправку данных в Kafka"""
    sample_data = {"id": "123", "name": "Test Record", "value": 42}

    # Отправляем данные
    send_data(sample_data)

    # Проверяем, что KafkaProducer.send был вызван 1 раз с нужными параметрами
    mock_kafka_producer.send.assert_called_once_with("data_stream", sample_data)

    # Проверяем, что flush был вызван
    mock_kafka_producer.flush.assert_called_once()
