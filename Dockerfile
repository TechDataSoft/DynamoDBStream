FROM python:3.11

# 2️⃣ Устанавливаем рабочую директорию
WORKDIR /app

# 3️⃣ Копируем файлы зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# 4️⃣ Копируем весь проект
COPY . .

# 5️⃣ Устанавливаем переменные окружения
ENV PYTHONPATH=/app

# 6️⃣ Открываем порт для FastAPI
EXPOSE 8000

# 7️⃣ Запускаем сервер (добавлен --reload для удобства в dev-режиме)
CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]

