def test_open_homepage(browser):
    browser.get("https://the-internet.herokuapp.com")
    assert "The Internet" in browser.title  # ✅ Should pass

def test_fail_example(browser):
    browser.get("https://the-internet.herokuapp.com")
    assert "Wrong Title" in browser.title  # ❌ This will fail to test screenshot feature
