from pages.checkboxes_page import CheckboxesPage

def test_checkboxes(browser):
    browser.get("https://the-internet.herokuapp.com/checkboxes")

    page = CheckboxesPage(browser)

    # Step 1: Select checkbox 1
    page.select_checkbox_1()
    assert page.is_checkbox_1_selected() is True

    # Step 2: Unselect checkbox 2
    page.unselect_checkbox_2()
    assert page.is_checkbox_2_selected() is False
