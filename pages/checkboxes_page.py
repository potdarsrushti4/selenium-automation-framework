from selenium.webdriver.common.by import By

class CheckboxesPage:

    CHECKBOX_1 = (By.XPATH, "//form[@id='checkboxes']/input[1]")
    CHECKBOX_2 = (By.XPATH, "//form[@id='checkboxes']/input[2]")

    def __init__(self, driver):
        self.driver = driver

    def select_checkbox_1(self):
        cb = self.driver.find_element(*self.CHECKBOX_1)
        if not cb.is_selected():
            cb.click()

    def unselect_checkbox_1(self):
        cb = self.driver.find_element(*self.CHECKBOX_1)
        if cb.is_selected():
            cb.click()

    def is_checkbox_1_selected(self):
        return self.driver.find_element(*self.CHECKBOX_1).is_selected()

    def select_checkbox_2(self):
        cb = self.driver.find_element(*self.CHECKBOX_2)
        if not cb.is_selected():
            cb.click()

    def unselect_checkbox_2(self):
        cb = self.driver.find_element(*self.CHECKBOX_2)
        if cb.is_selected():
            cb.click()

    def is_checkbox_2_selected(self):
        return self.driver.find_element(*self.CHECKBOX_2).is_selected()
