from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from login_page import LoginPage
from products_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop_po():

    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--start-maximized")

    driver = webdriver.Firefox(options=firefox_options)

    login_page = LoginPage(driver).open()
    login_page.login()

    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    products_page = ProductsPage(driver)
    for product in products:
        products_page.add_product_by_name(product)

    products_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_customer_info("Иван", "Петров", "101000")
    checkout_page.continue_checkout()

    total = checkout_page.get_total()
    assert total == "Total: $58.29", (
        f"Ожидалось 'Total: $58.29', а получили '{total}'")

    print("Тест пройден!")
    driver.quit()
