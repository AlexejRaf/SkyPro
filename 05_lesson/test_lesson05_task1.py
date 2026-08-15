from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")
    original_url = driver.current_url

    driver.find_element(By.PARTIAL_LINK_TEXT, "Form").click()
    time.sleep(2)

    assert "/forms/post" in driver.current_url, "URL не содержит /forms/post"

    driver.back()
    time.sleep(2)

    assert driver.current_url == original_url, (
        "Не удалось вернуться на главную")

    print("Тест пройден!")
    driver.quit()


if __name__ == "__main__":
    test_navigation()
