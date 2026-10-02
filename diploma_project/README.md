# Дипломный проект: Автотесты для YouGile

## Описание

Дипломный проект по автоматизации тестирования сервиса **YouGile**.
Проект включает:
- **API-тесты** (5 штук) — проверка работы REST API.
- **UI-тесты** (5 штук) — проверка интерфейса через Selenium.

Объект тестирования:
- Создание, получение, обновление задач через API.
- Авторизация через веб-интерфейс.

## Стек
- Python 3.10+
- pytest, requests, selenium, allure-pytest, python-dotenv

## Установка
1. Клонировать репозиторий.
2. `pip install -r requirements.txt`
3. Скопировать `.env.example` в `.env` и заполнить своими данными.

## Настройка окружения

В файле `.env` (создаётся из `.env.example`) нужно указать:
- `BASE_URL` — базовый URL API
- `API_TOKEN` — API-ключ YouGile
- `UI_URL` — URL главной страницы
- `UI_USERNAME` — email для входа
- `UI_PASSWORD` — пароль
- `COLUMN_ID` — ID колонки для создания задач
- `BOARD_ID` — ID доски
- `ASSIGNEE_ID` — ID исполнителя

## Запуск
- API-тесты: `pytest api_tests/ -v`
- UI-тесты: `pytest ui_tests/ -v`
- Все: `pytest -v`

## Отчёт Allure
1. `pytest --alluredir=allure-results`
2. `allure serve allure-results`

## Структура проекта
API-тесты: 5 тестов
Пройдено: 5/5

UI-тесты: 5 тестов
Пройдено: 5/5

Всего 10 тестов
Пройдено: 10/10