from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def setup_driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver

def test_successful_registration():

    driver = setup_driver()

    driver.get("http://localhost:3000/register")

    driver.find_element(By.ID, "name").send_keys("JohnDoe")
    driver.find_element(By.ID, "email").send_keys("john@example.com")
    driver.find_element(By.ID, "password").send_keys("Password1234")
    driver.find_element(By.ID, "confirmPassword").send_keys("Password1234")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(2)

    success = driver.find_element(By.CLASS_NAME, "success").text

    assert "Success" in success

    driver.quit()


def test_duplicate_email():

    driver = setup_driver()

    driver.get("http://localhost:3000/register")

    driver.find_element(By.ID, "name").send_keys("JohnDoe")
    driver.find_element(By.ID, "email").send_keys("john@example.com")
    driver.find_element(By.ID, "password").send_keys("Password1234")
    driver.find_element(By.ID, "confirmPassword").send_keys("Password1234")

    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    time.sleep(2)

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "already exists" in error

    driver.quit()