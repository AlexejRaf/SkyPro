# Lesson 10 — Page Object + Allure

Автотесты для сайтов:
- [Калькулятор](https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html)
- [Интернет-магазин SauceDemo](https://www.saucedemo.com/)

Проект использует:
- **pytest** — запуск тестов;
- **Selenium** — автоматизация браузера Chrome;
- **Allure** — генерация красивых отчётов;
- паттерн **Page Object** — логика страниц в отдельных классах.

---

## 📁 Структура проекта

```
lesson_10/
├── pages/                     # Page Object классы
│   ├── calculator_page.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── conftest.py                # фикстуры (драйвер Chrome)
├── test_calculator.py         # тест калькулятора
├── test_shop.py               # тест интернет-магазина
├── README.md
└── .gitignore
```

---

## 🛠️ Установка

Перед запуском тестов установи зависимости:

```bash
pip install pytest selenium allure-pytest
```

Также убедись, что установлен **Allure Commandline**.  
Проверить:
```bash
allure --version
```
Должна отобразиться версия, например `2.46.1`.

---

## 🚀 Запуск тестов

Перейди в папку `lesson_10`:

```bash
cd lesson_10
```

Запусти все тесты:

```bash
pytest -v
```

Или конкретный файл:

```bash
pytest test_calculator.py -v
pytest test_shop.py -v
```

---

## 📊 Формирование отчёта Allure

1. Запусти тесты с флагом `--alluredir`:

```bash
pytest --alluredir=allure-results
```

2. Сгенерируй и открой отчёт в браузере:

```bash
allure serve allure-results
```

Отчёт откроется автоматически по адресу `http://127.0.0.1:xxxx`.

---

## 📂 Что НЕ нужно пушить

Папки `allure-results` и `allure-report` указаны в `.gitignore` — они создаются автоматически при запуске и не должны попадать в репозиторий.

---

## 📌 Что проверяют тесты

### `test_calculator.py`
- Устанавливает задержку 45 секунд.
- Нажимает `7 + 8 =`.
- Проверяет, что результат равен `15`.

### `test_shop.py`
- Авторизуется как `standard_user`.
- Добавляет три товара в корзину.
- Оформляет заказ.
- Проверяет, что итоговая сумма равна `Total: $58.29`.