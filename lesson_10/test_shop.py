"""Тесты для интернет-магазина SauceDemo с отчётом Allure."""
import allure

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.title("Покупка трёх товаров с проверкой итоговой суммы")
@allure.description(
    "Авторизуемся как standard_user, добавляем три товара в корзину, "
    "оформляем заказ и проверяем, что итоговая сумма равна $58.29."
)
@allure.severity(allure.severity_level.BLOCKER)
def test_shop(driver):
    """Тест проверяет полный цикл покупки в интернет-магазине."""
    products = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
    ]

    with allure.step("Авторизоваться как standard_user"):
        login_page = LoginPage(driver).open()
        login_page.login()

    with allure.step("Добавить три товара в корзину"):
        products_page = ProductsPage(driver)
        for product in products:
            products_page.add_product_by_name(product)

    with allure.step("Перейти в корзину"):
        products_page.go_to_cart()

    with allure.step("Нажать кнопку Checkout"):
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

    with allure.step("Заполнить форму данными покупателя"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_customer_info("Иван", "Петров", "101000")

    with allure.step("Нажать Continue и перейти к итогам"):
        checkout_page.continue_checkout()

    with allure.step("Проверить, что итоговая сумма равна $58.29"):
        total = checkout_page.get_total()
        assert total == "Total: $58.29", (
            f"Ожидалось 'Total: $58.29', получено '{total}'"
        )
