"""Page Object для страницы товаров SauceDemo."""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    """Класс страницы со списком товаров."""

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BTN = (By.ID, "checkout")

    def __init__(self, driver: Chrome) -> None:
        """Инициализирует страницу.

        Args:
            driver: WebDriver Chrome.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_by_name(self, product_name: str) -> "ProductsPage":
        """Добавляет товар в корзину по названию.

        Args:
            product_name: название товара.

        Returns:
            ProductsPage: текущий объект страницы.
        """
        product = self.driver.find_element(
            By.XPATH, f"//div[text()='{product_name}']"
        )
        add_button = product.find_element(
            By.XPATH,
            "./ancestor::div[@class='inventory_item']//button",
        )
        add_button.click()
        return self

    def go_to_cart(self) -> "ProductsPage":
        """Переходит в корзину.

        Returns:
            ProductsPage: текущий объект страницы.
        """
        self.driver.find_element(*self.CART_LINK).click()
        self.wait.until(
            EC.presence_of_element_located(self.CHECKOUT_BTN)
        )
        return self
