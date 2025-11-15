from selenium.webdriver.common.by import By

class FlipkartSearchResultsPage:

    PRODUCT_TITLES = (By.CSS_SELECTOR, "div.KzDlHZ")

    def __init__(self, driver):
        self.driver = driver

    def get_first_product_title(self):
        items = self.driver.find_elements(*self.PRODUCT_TITLES)
        if not items:
            self.driver.save_screenshot("flipkart_debug.png")
            raise Exception("No Flipkart product titles found!")

        return items[0].text
