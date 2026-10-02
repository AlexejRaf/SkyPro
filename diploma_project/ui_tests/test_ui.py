"""UI-тесты для YouGile."""
import os

import allure
import pytest
from selenium.webdriver import Chrome

from pages.login_page import LoginPage


@pytest.fixture
def login_page(driver: Chrome) -> LoginPage:
    """Создаёт LoginPage для тестов.

    Args:
        driver: драйвер Chrome.

    Returns:
        LoginPage: страница авторизации.
    """
    url = os.getenv("UI_URL", "https://ru.yougile.com")
    return LoginPage(driver, url)


@allure.feature("YouGile UI: Авторизация")
@allure.title("Открытие формы логина")
@allure.severity(allure.severity_level.CRITICAL)
def test_open_login_form(login_page: LoginPage) -> None:
    """Позитивный: форма логина открывается."""
    with allure.step("Открыть главную и нажать 'Войти'"):
        login_page.open()
    with allure.step("Проверить, что поля логина видны"):
        assert login_page.driver.find_elements(
            *login_page.EMAIL_INPUT
        ), "Поле email не найдено"


@allure.feature("YouGile UI: Авторизация")
@allure.title("Успешная авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_positive(login_page: LoginPage) -> None:
    """Позитивный: вход с валидными данными."""
    with allure.step("Открыть форму логина"):
        login_page.open()
    with allure.step("Войти с валидными данными"):
        login_page.login(
            os.getenv("UI_USERNAME", ""),
            os.getenv("UI_PASSWORD", ""),
        )
    with allure.step("Проверить, что пользователь вошёл"):
        assert login_page.is_logged_in(), "Не удалось войти"


@allure.feature("YouGile UI: Авторизация")
@allure.title("Неуспешная авторизация")
@allure.severity(allure.severity_level.NORMAL)
def test_login_negative(login_page: LoginPage) -> None:
    """Негативный: вход с неверным паролем."""
    with allure.step("Открыть форму логина"):
        login_page.open()
    with allure.step("Войти с неверным паролем"):
        login_page.login(
            os.getenv("UI_USERNAME", ""),
            "wrong_password_12345",
        )
    with allure.step("Проверить, что форма логина осталась"):
        assert login_page.is_error_displayed(), (
            "Пользователь вошёл с неверным паролем!"
        )


@allure.feature("YouGile UI: Авторизация")
@allure.title("Проверка URL после клика 'Войти'")
@allure.severity(allure.severity_level.NORMAL)
def test_sign_in_button_works(login_page: LoginPage) -> None:
    """Позитивный: клик по 'Войти' открывает форму."""
    with allure.step("Открыть главную и кликнуть 'Войти'"):
        login_page.open()
    with allure.step("Проверить наличие поля пароля"):
        assert login_page.driver.find_elements(
            *login_page.PASSWORD_INPUT
        ), "Поле пароля не найдено"


@allure.feature("YouGile UI: Авторизация")
@allure.title("Проверка заголовка страницы")
@allure.severity(allure.severity_level.MINOR)
def test_page_title(login_page: LoginPage) -> None:
    """Позитивный: заголовок страницы непустой."""
    with allure.step("Открыть главную"):
        login_page.open()
    with allure.step("Проверить заголовок"):
        assert login_page.driver.title, "Заголовок страницы пустой"
