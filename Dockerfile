FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /code

# 1. ОБНОВЛЕНИЕ: Устанавливаем системные зависимости (gcc, libxml, и т.д.)
# Это нужно для сборки newspaper3k и lxml
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libxml2-dev \
    libxslt-dev \
    libjpeg-dev \
    zlib1g-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# 2. Копируем requirements и устанавливаем python-библиотеки
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Копируем код приложения
COPY . .

# Команда запуска
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]