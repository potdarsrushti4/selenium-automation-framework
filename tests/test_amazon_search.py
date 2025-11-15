from pages.amazon_home_page import AmazonHomePage
from pages.amazon_search_results_page import AmazonSearchResultsPage

def test_amazon_search_product(browser):
    home = AmazonHomePage(browser)
    results = AmazonSearchResultsPage(browser)

    home.load()
    browser.save_screenshot("amazon_home_debug.png")
    home.search_product("iPhone 14")

    title = results.get_first_product_title()
    assert "iPhone" in title
