from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FlipkartHomePage:

    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.CLASS_NAME, "_2iLD__")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get("https://www.flipkart.com")

    def search_product(self, product_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        ).send_keys(product_name)

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SEARCH_BUTTON)
        ).click()
