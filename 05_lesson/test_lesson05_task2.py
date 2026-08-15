from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    driver.find_element(By.NAME, "custname").send_keys("Иван Иванов")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    assert "/post" in driver.current_url, "URL не изменился"

    print("Тест пройден!")
    driver.quit()


if __name__ == "__main__":
    test_form_submission()
