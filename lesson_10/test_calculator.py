"""Тесты для медленного калькулятора с отчётом Allure."""
import allure

from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.title("Проверка работы медленного калькулятора")
@allure.description(
    "Открываем страницу калькулятора, устанавливаем задержку 45 секунд, "
    "выполняем 7 + 8 = и проверяем, что результат равен 15."
)
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator(driver):
    """Тест проверяет работу калькулятора с задержкой 45 секунд."""
    page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        page.open()

    with allure.step("Установить задержку 45 секунд"):
        page.set_delay("45")

    with allure.step("Нажать кнопки: 7, +, 8, ="):
        page.click_7()
        page.click_plus()
        page.click_8()
        page.click_equals()

    with allure.step("Дождаться появления результата 15"):
        page.wait_for_result("15", timeout=60)

    with allure.step("Проверить, что результат равен 15"):
        result = page.get_result()
        assert result == "15", (
            f"Ожидалось '15', получено '{result}'"
        )
