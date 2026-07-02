from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver

def test_dashboard_without_login():

    driver = setup_driver()

    driver.get("http://localhost:3000/dashboard")

    assert "login" in driver.current_url.lower()

    driver.quit()