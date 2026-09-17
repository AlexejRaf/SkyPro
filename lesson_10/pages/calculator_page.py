"""Page Object для страницы медленного калькулятора."""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Класс страницы медленного калькулятора."""

    URL = (
        "https://bonigarcia.dev/selenium-webdriver-java/"
        "slow-calculator.html"
    )

    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: Chrome) -> None:
        """Инициализирует страницу.

        Args:
            driver: WebDriver Chrome.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self) -> "CalculatorPage":
        """Открывает страницу калькулятора.

        Returns:
            CalculatorPage: текущий объект страницы.
        """
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds: str) -> None:
        """Устанавливает задержку вычисления.

        Args:
            seconds: задержка в секундах (строка).
        """
        field = self.driver.find_element(*self.DELAY_INPUT)
        field.clear()
        field.send_keys(seconds)

    def click_7(self) -> None:
        """Нажимает кнопку 7."""
        self.driver.find_element(*self.BUTTON_7).click()

    def click_8(self) -> None:
        """Нажимает кнопку 8."""
        self.driver.find_element(*self.BUTTON_8).click()

    def click_plus(self) -> None:
        """Нажимает кнопку +."""
        self.driver.find_element(*self.BUTTON_PLUS).click()

    def click_equals(self) -> None:
        """Нажимает кнопку =."""
        self.driver.find_element(*self.BUTTON_EQUALS).click()

    def wait_for_result(self, expected: str, timeout: int = 60) -> None:
        """Ждёт появления результата на экране.

        Args:
            expected: ожидаемый текст на экране.
            timeout: максимальное время ожидания (секунды).
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.RESULT_SCREEN, expected
            )
        )

    def get_result(self) -> str:
        """Возвращает текст с экрана калькулятора.

        Returns:
            str: результат вычисления.
        """
        return self.driver.find_element(*self.RESULT_SCREEN).text
