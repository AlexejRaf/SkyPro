from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product_by_name(self, product_name):

        product = self.driver.find_element(
            By.XPATH, f"//div[text()='{product_name}']")

        add_button = product.find_element(
            By.XPATH, "./ancestor::div[@class='inventory_item']//button"
        )
        add_button.click()
        return self

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        return self
