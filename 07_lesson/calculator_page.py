from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CalculatorPage:

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    DELAY_INPUT = (By.ID, "delay")
    BTN_7 = (By.XPATH, "//span[text()='7']")
    BTN_8 = (By.XPATH, "//span[text()='8']")
    BTN_PLUS = (By.XPATH, "//span[text()='+']")
    BTN_EQUALS = (By.XPATH, "//span[text()='=']")
    RESULT = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def set_delay(self, seconds):
        field = self.driver.find_element(*self.DELAY_INPUT)
        field.clear()
        field.send_keys(seconds)

    def click_7(self):
        self.driver.find_element(*self.BTN_7).click()

    def click_8(self):
        self.driver.find_element(*self.BTN_8).click()

    def click_plus(self):
        self.driver.find_element(*self.BTN_PLUS).click()

    def click_equals(self):
        self.driver.find_element(*self.BTN_EQUALS).click()
        time.sleep(0.5)

    def wait_for_result(self, expected_text, timeout=60):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.RESULT, expected_text)
        )

    def get_result(self):
        return self.driver.find_element(*self.RESULT).text
