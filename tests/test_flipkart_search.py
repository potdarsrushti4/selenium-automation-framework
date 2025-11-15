from pages.flipkart_home_page import FlipkartHomePage
from pages.flipkart_search_results_page import FlipkartSearchResultsPage

def test_flipkart_product_search(browser):
    home = FlipkartHomePage(browser)
    results = FlipkartSearchResultsPage(browser)

    home.load()
    home.search_product("iPhone 14")

    title = results.get_first_product_title()
    assert "iPhone" in title or "Apple" in title