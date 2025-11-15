import pytest
from pages.parabank_login_page import ParabankLoginPage

@pytest.mark.bank
def test_parabank_valid_login(browser):
    login = ParabankLoginPage(browser)
    login.load()
    login.login("john", "demo")  # Parabank demo credentials
    assert login.is_login_successful()