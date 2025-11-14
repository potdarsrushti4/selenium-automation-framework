import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture
#This function provides setup data or a resource that other tests can use.
def browser():
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Users\srushti potdar\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
    service = Service(ChromeDriverManager(driver_version="142.0.7444.60").install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # If test failed, take screenshot
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{item.name}.png"
            destination_file = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(destination_file)
            # Attach to pytest-html report
            if hasattr(rep, "extra"):
                from pytest_html import extras
                rep.extra.append(extras.image(destination_file))
