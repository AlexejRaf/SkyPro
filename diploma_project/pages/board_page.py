"""Page Object страницы проекта (доски с задачами)."""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BoardPage:
    """Страница проекта с задачами."""

    # Локаторы
    CREATE_TASK_BUTTON = (
        By.XPATH, "//button[contains(text(), 'Создать задачу')]"
    )
    TASK_TITLE_INPUT = (
        By.CSS_SELECTOR, "textarea[placeholder*='название']"
    )
    SAVE_BUTTON = (
        By.XPATH, "//button[contains(text(), 'Сохранить')]"
    )

    def __init__(self, driver: Chrome) -> None:
        """Инициализация страницы.

        Args:
            driver: драйвер Chrome.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def open_project(self, project_url: str) -> "BoardPage":
        """Открывает проект по URL.

        Args:
            project_url: URL проекта.

        Returns:
            BoardPage: текущая страница.
        """
        self.driver.get(project_url)
        return self

    def create_task(self, title: str) -> None:
        """Создаёт задачу с указанным названием.

        Args:
            title: название задачи.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CREATE_TASK_BUTTON)
        ).click()

        title_field = self.wait.until(
            EC.visibility_of_element_located(self.TASK_TITLE_INPUT)
        )
        title_field.send_keys(title)

        self.driver.find_element(*self.SAVE_BUTTON).click()

    def is_task_present(self, title: str) -> bool:
        """Проверяет, есть ли задача с указанным названием.

        Args:
            title: название задачи.

        Returns:
            bool: True, если задача найдена.
        """
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, f"//*[contains(text(), '{title}')]")
                )
            )
            return True
        except Exception:
            return False