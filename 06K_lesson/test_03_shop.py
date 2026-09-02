from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    # Открываем браузер Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    # --- 1. Авторизация ---
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Ждём загрузки страницы с товарами
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    # --- 2. Добавляем товары в корзину ---
    # Названия товаров
    products = [
        "Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"
        ]

    for product_name in products:
        product = driver.find_element(
            By.XPATH, f"//div[text()='{product_name}']")
        add_button = product.find_element(
            By.XPATH, "./ancestor::div[@class='inventory_item']//button")
        add_button.click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("101000")

    driver.find_element(By.ID, "continue").click()

    total = driver.find_element(By.CLASS_NAME, "summary_total_label").text

    assert total == "Total: $58.29", f"Ожидалось 'Total: $58.29', а получили '{
        total}'"

    print("Тест пройден!")
    driver.quit()
