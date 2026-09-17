"""Page Object для страницы авторизации SauceDemo."""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Класс страницы авторизации."""

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")

    def __init__(self, driver: Chrome) -> None:
        """Инициализирует страницу.

        Args:
            driver: WebDriver Chrome.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> "LoginPage":
        """Открывает страницу авторизации.

        Returns:
            LoginPage: текущий объект страницы.
        """
        self.driver.get(self.URL)
        return self

    def login(
        self,
        username: str = "standard_user",
        password: str = "secret_sauce",
    ) -> None:
        """Выполняет вход в систему.

        Args:
            username: имя пользователя.
            password: пароль.
        """
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

        self.wait.until(
            EC.presence_of_element_located(self.INVENTORY_LIST)
        )
