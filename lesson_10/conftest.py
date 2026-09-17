"""Фикстуры для тестов: драйвер Chrome, Allure-скриншоты."""
from typing import Generator

import allure
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture()
def driver() -> Generator[Chrome, None, None]:
    """Создаёт и возвращает драйвер Chrome.

    Yields:
        Chrome: настроенный драйвер браузера.
    """
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    drv = Chrome(options=options)
    yield drv

    if hasattr(drv, "_failed") and drv._failed:
        allure.attach(
            drv.get_screenshot_as_png(),
            name="Скриншот при падении",
            attachment_type=allure.attachment_type.PNG,
        )
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook: помечает тест как упавший, если он упал.

    Args:
        item: тестовый айтем.
        call: фаза запуска теста.
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            driver_fixture._failed = True
