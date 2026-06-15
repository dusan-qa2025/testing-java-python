# fajl obuhvata vise test scenarija
# 1. test_login_without_data()
# 2. test_login_without_password()
# 3. test_login_with_wrong_credentials()
# 4. test_successful_login()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

BASE_URL = "https://www.saucedemo.com/"

# Helper funkcije
# -------------------------------------------
def create_driver():
    options = Options()
    prefs = {
        "credentials_enable_service":False,
        "profile.password_manager_enabled":False,
        "profile.password_manager_leak_detection":False
    }
    options.add_experimental_option("prefs", prefs)

    # instanciranje drivera (browser - sa podesavanjima)
    driver = webdriver.Chrome(options=options)
    return driver

def create_wait(driver):
    wait = WebDriverWait(driver, 10)
    return wait

def open_login_page(driver):
    driver.get(BASE_URL)

# izvuci dobavljanje error poruke u odvojenu funkciju
# def get_error_msg(wait): return error_msg


# funkcija locira elemente, popunjava polja i izvrsava klik 
def login(driver, username, password):
    # unosimo user name
    user_text_field = driver.find_element(By.ID, "user-name")
    user_text_field.send_keys(username) # pogresan user name
    # unosimo password
    password_text_field = driver.find_element(By.ID, "password")
    password_text_field.send_keys(password) # pogresan password
    # klik na taster
    driver.find_element(By.ID, "login-button").click()

# Test funkcije
# --------------------------------------------------
def test_login_without_data():
    driver = create_driver()
    wait = create_wait(driver)
    open_login_page(driver)
    login(driver, "", "") # prazni kredencijali

    # izvuci dobavljanje error poruke u odvojenu funkciju
    error_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    #assert ostaje ovde 
    assert "Username is required" in error_message.text  
    time.sleep(5)
    driver.quit()

def test_login_without_password():
    driver = create_driver()
    wait = create_wait(driver)
    open_login_page(driver)
    login(driver, "standard_user", "")
    error_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    assert "Password is required" in error_message.text
    time.sleep(5)
    driver.quit()

def test_login_with_wrong_credentials():
    driver = create_driver()
    wait = create_wait(driver)
    open_login_page(driver)
    login(driver, "test", "123")
    error_message = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
    )
    print(error_message.text)
    assert "Epic sadface: Username and password do not match any user in this service" == error_message.text.strip()
    time.sleep(5)
    driver.quit()

def test_successful_login():
    driver = create_driver()
    wait = create_wait(driver)
    open_login_page(driver)

    login(driver, "standard_user", "secret_sauce")

    title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert title.text == "Products"

    time.sleep(5)
    driver.quit()

test_login_without_password()
test_login_with_wrong_credentials()
test_login_without_data()
test_successful_login()