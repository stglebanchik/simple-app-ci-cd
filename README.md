# Flask CI/CD Simple example
Автоматизация сборки и запуска проекта на GitHub + Docker (цифровая кафедра)

Этот репозиторий демонстрирует настройку непрерывной интеграции и доставки (CI/CD) для простого Flask-приложения с использованием Docker и GitHub Actions.

[![CI Status](https://github.com/stglebanchik/simple-app-ci-cd/actions/workflows/docker-ci.yml/badge.svg?branch=main)](https://github.com/stglebanchik/simple-app-ci-cd/actions/workflows/docker-ci.yml)

## 📦 Файлы проекта

- **Dockerfile** — описание сборки образа  
- **app.py** — исходник Flask‑сервера  
- **requirements.txt** — зависимости Python  
- **.github/workflows/docker-ci.yml** — workflow для CI/CD  


## 🛠️ Сборка и запуск локально

1. **Клонировать репозиторий**  
   ```bash
   git clone https://github.com/stglebanchik/simple-app-ci-cd.git
   cd simple-app-ci-cd

2. **Построить образ**
    ```bash
    docker build -t simple‑flask‑app .

3. **Запустить контейнер**
    ```bash
    docker run --rm -d -p 5000:5000 --name flask‑app simple‑flask‑app  

4. **Проверить работу**
    
    В браузере: http://localhost:5000

    Или в терминале: curl http://localhost:5000
    
    Вы должны увидеть: Hello, World from Docker and GitHub Actions!

5. **Остановка и удаление контейнера**
    ```bash
    docker stop flask‑app

## ⚙️ Как устроен Dockerfile
- FROM python:3.12-slim — лёгкий базовый образ с Python 3.12
- RUN apt-get install gcc — компилятор для пакетов с нативными модулями
- WORKDIR /app — рабочая директория
- COPY requirements.txt . + pip install -r requirements.txt — установка зависимостей
- COPY . . — копирование всего содержимого текущей директории (кроме .dockerignore)
- EXPOSE 5000 — документирование порта
- CMD ["python3","app.py"] — команда запуска

## 🤖 Описание GitHub Actions Workflow
- Файл: .github/workflows/docker-ci.yml
- Триггер: push или pull_request ↦ ветка main
    # Шаги:
    1. Checkout code — actions/checkout@v4
    2. Setup Buildx — docker/setup-buildx-action@v2
    3. Build image — docker/build-push-action@v4
        - Тег: simple-flask-app:ci
        - load: true для последующего запуска
        - Кэш сборки в GitHub Actions
    4. Smoke‑test
        - Запускает контейнер на порту 5000
        - Ждёт 5 секунд
        - Делает curl и проверяет HTTP-код 200
        - Останавливает контейнер и падает при ошибке
