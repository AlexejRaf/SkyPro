"""Page Object страницы авторизации YouGile."""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """Страница авторизации YouGile."""

    # Локаторы
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".sign-in-button")
    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        "input[type='email'][placeholder='example@mail.ru']",
    )
    PASSWORD_INPUT = (
        By.CSS_SELECTOR,
        "input[type='password'][placeholder='Введите пароль']",
    )

    def __init__(self, driver: Chrome, url: str) -> None:
        """Инициализация страницы.

        Args:
            driver: драйвер Chrome.
            url: URL главной страницы YouGile.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 15)

    def open(self) -> "LoginPage":
        """Открывает главную и кликает 'Войти'.

        Returns:
            LoginPage: текущая страница.
        """
        self.driver.get(self.url)

        sign_in = self.wait.until(
            EC.element_to_be_clickable(self.SIGN_IN_BUTTON)
        )
        sign_in.click()

        # Ждём появления формы логина
        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        return self

    def login(self, email: str, password: str) -> None:
        """Вводит данные и отправляет форму.

        Args:
            email: email пользователя.
            password: пароль пользователя.
        """
        email_field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_INPUT)
        )
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.driver.find_element(*self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        # Отправляем форму через Enter
        password_field.send_keys(Keys.ENTER)

    def is_logged_in(self) -> bool:
        """Проверяет, что пользователь вошёл.

        Returns:
            bool: True, если URL указывает на рабочее пространство.
        """
        try:
            self.wait.until(
                lambda d: "login" not in d.current_url.lower()
            )
            return True
        except Exception:
            return False

    def is_error_displayed(self) -> bool:
        """Проверяет, что остались на странице логина (значит, ошибка).

        Returns:
            bool: True, если форма логина всё ещё видна.
        """
        try:
            self.driver.find_element(*self.PASSWORD_INPUT)
            return True
        except Exception:
            return False