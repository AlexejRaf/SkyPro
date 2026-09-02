from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "zip-code": "",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "form"))
    )

    for name, value in form_data.items():
        field = driver.find_element(By.NAME, name)
        field.clear()
        if value:
            field.send_keys(value)

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    driver.execute_script("arguments[0].click();", submit_button)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".alert-danger, .alert-success"))
    )

    red_blocks = driver.find_elements(By.CSS_SELECTOR, ".alert-danger")
    assert len(red_blocks) > 0, "Нет красных полей (Zip code не подсвечен)"

    green_blocks = driver.find_elements(By.CSS_SELECTOR, ".alert-success")
    assert len(green_blocks) >= 9, f"Найдено {
        len(green_blocks)} зелёных полей, ожидалось 9"

    print("Тест пройден!")
    driver.quit()
