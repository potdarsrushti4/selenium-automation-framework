from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonSearchResultsPage:

    PRODUCT_TITLES = (
        By.CSS_SELECTOR,
        "span.a-size-medium.a-color-base.a-text-normal"
    )

    def __init__(self, driver):
        self.driver = driver

    def get_first_product_title(self):
        products = self.driver.find_elements(*self.PRODUCT_TITLES)

        if not products:
            # Save screenshot for debugging
            self.driver.save_screenshot("no_titles_debug.png")
            raise Exception("No product titles found! Amazon UI probably changed.")

        return products[0].text