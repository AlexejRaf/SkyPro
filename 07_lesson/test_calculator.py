from selenium import webdriver
from calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    driver.maximize_window()

    page = CalculatorPage(driver)
    page.open()
    page.set_delay("45")
    page.click_7()
    page.click_plus()
    page.click_8()
    page.click_equals()

    # Ждём результат до 60 секунд
    page.wait_for_result("15", timeout=60)

    result = page.get_result()
    assert result == "15", f"Ожидалось 15, а получили {result}"

    driver.quit()
