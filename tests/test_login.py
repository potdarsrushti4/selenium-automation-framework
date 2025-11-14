from pages.login_page import LoginPage

def test_valid_login(browser):
    browser.get("https://the-internet.herokuapp.com/login")

    login = LoginPage(browser)
    login.login("tomsmith", "SuperSecretPassword!")

    assert login.is_success_message_displayed()
