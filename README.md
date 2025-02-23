# DynamoDB Stream Processor

## 🔥 О проекте  
**DynamoDB Stream Processor** — это высоконагруженный сервис для обработки потоков данных из SQLite с использованием Apache Kafka.  
Проект разработан для трека **"Обработка и хранение данных"** грантовой программы **Yandex Open Source**.

### **🚀 Возможности**
✅ Получение и обработка изменений в DynamoDB в режиме реального времени.  
✅ Производитель (`Producer`) отправляет данные в Apache Kafka.  
✅ Потребитель (`Consumer`) обрабатывает данные и сохраняет их в хранилище.  
✅ Поддержка кэширования для повышения производительности.  
✅ Гибкая конфигурация через `.env` и `config.yaml`.  
✅ Логирование и мониторинг событий.

---

## 🛠️ Технологии
- **Kafka** – брокер сообщений
- **Zookeeper** – координация Kafka
- **Redis** – кэширование и хранение данных
- **SQLite** – встроенная база данных для API
- **API (Flask или другой backend)** – обработка данных
- **Kafdrop** – UI для Kafka
- **Kafka UI** – мониторинг и управление кластерами Kafka

## 📦 Сервисы
- `zookeeper` – сервис для управления Kafka
- `kafka` – брокер сообщений
- `redis` – in-memory хранилище
- `api` – бекенд-сервис с поддержкой Kafka, Redis и SQLite
- `kafdrop` – веб-интерфейс для Kafka
- `kafka-ui` – UI-инструмент для управления Kafka

---

## 📂 Структура проекта

DynamoDBStream/
│── app/                  # Основная логика приложения
│   ├── api.py            # API для мониторинга и тестирования
│   ├── cache.py          # Работа с Redis-кэшем
│   ├── config.py         # Конфигурация проекта
│   ├── consumer.py       # Обработчик Kafka (Consumer)
│   ├── db.py             # Подключение к базе данных
│   ├── producer.py       # Отправка сообщений в Kafka (Producer)
│
│── tests/                # Тесты
│   ├── __init__.py       # Инициализация модуля
│   ├── test_producer.py  # Тестирование Producer
│
│── .env                  # Файл переменных окружения
│── config.yaml           # Основные настройки проекта
│── docker-compose.yml    # Запуск проекта в контейнерах
│── pytest.ini            # Конфигурация Pytest
│── README.md             # Описание проекта
│── requirements.txt      # Список зависимостей


## ⚙️ Установка и запуск  

### **1️⃣ Клонирование репозитория**
```bash
git clone https://github.com/YOUR_USERNAME/DynamoDBStream.git
cd DynamoDBStream

2️⃣ Установка зависимостей
pip install -r requirements.txt


3️⃣ Запуск Kafka и Redis через Docker
docker-compose up -d


## 🔧 Конфигурация
- Kafka автоматически создает топики
- Данные Kafka хранятся в `./kafka-data`
- API использует SQLite (`/data/database.sqlite`)
- Доступ к Kafka UI: `http://localhost:8080` (логин: `admin`, пароль: `strongpassword123`)
- Доступ к Kafdrop: `http://localhost:9000`

## 📬 API Эндпоинты
### Получение всех сообщений
```
GET http://localhost:5000/latest-messages
```

### Отправка сообщения
```
POST http://localhost:5000/send/
Content-Type: application/json

{
    "id": "12",
    "name": "Hello messages",
    "value": 111
}
```

### Получение сообщения по ID
```
GET http://localhost:5000/record/12
```

5️⃣ Запуск тестов
pytest tests/


📜 Лицензия
Проект распространяется под лицензией MIT.