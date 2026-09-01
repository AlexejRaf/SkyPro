from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    # 2. Найдите и нажмите на кнопку "Start"
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div#start button"))
    )
    start_button.click()
    # 3. Дождитесь появления текста "Hello World!"
    finish_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div#finish"))
    ).text
    # 4. Сделайте скриншот страницы
    driver.save_screenshot("screenshots/page.png")
    # 5. Проверьте, что появившийся текст равен "Hello World!"
    expected_text = "Hello World!"
    assert finish_text == expected_text, (
        f"Ожидался '{expected_text}', получен {finish_text}"
    )
    driver.quit()
