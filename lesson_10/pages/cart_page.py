"""Page Object для страницы корзины SauceDemo."""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Класс страницы корзины."""

    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")

    def __init__(self, driver: Chrome) -> None:
        """Инициализирует страницу.

        Args:
            driver: WebDriver Chrome.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def proceed_to_checkout(self) -> "CartPage":
        """Нажимает кнопку Checkout.

        Returns:
            CartPage: текущий объект страницы.
        """
        self.driver.find_element(*self.CHECKOUT_BTN).click()
        self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        return self
