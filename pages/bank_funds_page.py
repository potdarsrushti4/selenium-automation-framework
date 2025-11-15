from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BankFundsTransferPage:

    FUND_TRANSFER_LINK = (By.LINK_TEXT, "Fund Transfer")
    PAYER_ACC = (By.NAME, "payersaccount")
    PAYEE_ACC = (By.NAME, "payeeaccount")
    AMOUNT = (By.NAME, "ammount")
    DESC = (By.NAME, "desc")
    SUBMIT_BTN = (By.NAME, "AccSubmit")
    SUCCESS_MSG = (By.XPATH, "//p[contains(text(),'Fund Transfer Successful')]")

    def __init__(self, driver):
        self.driver = driver

    def open_fund_transfer_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.FUND_TRANSFER_LINK)
        ).click()

    def transfer_funds(self, payer, payee, amount, desc="Test"):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PAYER_ACC)
        )
        self.driver.find_element(*self.PAYER_ACC).send_keys(payer)
        self.driver.find_element(*self.PAYEE_ACC).send_keys(payee)
        self.driver.find_element(*self.AMOUNT).send_keys(amount)
        self.driver.find_element(*self.DESC).send_keys(desc)
        self.driver.find_element(*self.SUBMIT_BTN).click()

    def is_transfer_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.SUCCESS_MSG)
            )
            return True
        except:
            return False