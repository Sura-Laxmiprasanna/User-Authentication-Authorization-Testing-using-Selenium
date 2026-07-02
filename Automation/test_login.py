from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver


def test_successful_login():

    driver = setup_driver()

    driver.get("http://localhost:3000/login")

    driver.find_element(By.ID, "email").send_keys("sura@gmail.com")
    driver.find_element(By.ID, "password").send_keys("Password1234")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(2)

    assert "dashboard" in driver.current_url.lower()

    driver.quit()


def test_invalid_password():

    driver = setup_driver()

    driver.get("http://localhost:3000/login")

    driver.find_element(By.ID, "email").send_keys("sura@gmail.com")
    driver.find_element(By.ID, "password").send_keys("WrongPassword")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(2)

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "Unauthorized" in error

    driver.quit()