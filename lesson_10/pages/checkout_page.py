"""Page Object для страницы оформления заказа SauceDemo."""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Класс страницы оформления заказа."""

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver: Chrome) -> None:
        """Инициализирует страницу.

        Args:
            driver: WebDriver Chrome.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_customer_info(
        self,
        first_name: str,
        last_name: str,
        postal_code: str,
    ) -> "CheckoutPage":
        """Заполняет форму данными покупателя.

        Args:
            first_name: имя покупателя.
            last_name: фамилия покупателя.
            postal_code: почтовый индекс.

        Returns:
            CheckoutPage: текущий объект страницы.
        """
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        return self

    def continue_checkout(self) -> "CheckoutPage":
        """Нажимает Continue и ждёт страницу с итоговой суммой.

        Returns:
            CheckoutPage: текущий объект страницы.
        """
        self.driver.find_element(*self.CONTINUE_BTN).click()
        self.wait.until(
            EC.presence_of_element_located(self.TOTAL_LABEL)
        )
        return self

    def get_total(self) -> str:
        """Возвращает текст с итоговой суммой.

        Returns:
            str: строка вида "Total: $58.29".
        """
        return self.driver.find_element(*self.TOTAL_LABEL).text
