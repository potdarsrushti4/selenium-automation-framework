from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonHomePage:
    URL = "https://www.amazon.in"

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)
        self.handle_continue_shopping()

    def handle_continue_shopping(self):
        """Handles Amazon anti-bot Continue Shopping page."""
        try:
            button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "continue"))
            )
            button.click()
            print("✔ Continue shopping clicked")
        except:
            print("ℹ No continue shopping popup")

    def search_product(self, product_name):
        self.handle_continue_shopping()  # Ensure popup is cleared

        search_box = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, "twotabsearchtextbox"))
        )
        search_box.send_keys(product_name)

        search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()
