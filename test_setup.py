from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Users\srushti potdar\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"  # Check this path on your PC

service = Service(ChromeDriverManager(driver_version="142.0.7444.60").install())

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://the-internet.herokuapp.com")
print("✅ Opened site successfully in Brave!")
driver.quit()