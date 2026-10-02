# Дипломный проект: Автотесты для YouGile

## Стек
- Python 3.10+
- pytest, requests, selenium, allure-pytest, python-dotenv

## Установка
1. Клонировать репозиторий.
2. `pip install -r requirements.txt`
3. Скопировать `.env.example` в `.env` и заполнить своими данными.

## Запуск
- API-тесты: `pytest api_tests/ -v`
- UI-тесты: `pytest ui_tests/ -v`
- Все: `pytest -v`

## Отчёт Allure
1. `pytest --alluredir=allure-results`
2. `allure serve allure-results`