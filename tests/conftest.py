import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import yaml
import os

# Paths for different browsers
BRAVE_PATH = r"C:\Users\srushti potdar\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

def load_config():
    config_path = os.path.join("config", "config.yaml")
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

@pytest.fixture
def browser():
    config = load_config()
    browser_name = config.get("browser", "chrome").lower()

    options = webdriver.ChromeOptions()

    # USE THE CORRECT BROWSER BINARY
    if browser_name == "brave":
        options.binary_location = BRAVE_PATH
    elif browser_name == "edge":
        options.binary_location = EDGE_PATH

    # FIX: FORCE WEBDRIVER TO MATCH YOUR INSTALLED VERSION (142)
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(driver_version="142.0.7444.60").install()),
        options=options
    )

    driver.maximize_window()
    yield driver
    driver.quit()

# Screenshot hook
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("browser")
        if driver:
            screenshot_dir = os.path.join(os.getcwd(), "reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            file_name = f"{item.name}.png"
            destination_file = os.path.join(screenshot_dir, file_name)
            driver.save_screenshot(destination_file)

            if hasattr(rep, "extra"):
                from pytest_html import extras
                rep.extra.append(extras.image(destination_file))
