from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import getpass
from selenium.webdriver.common.keys import Keys

LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"

def create_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def wait_for(driver, by, value):
    wait = WebDriverWait(driver, 10)

    return wait.until(
        EC.visibility_of_element_located((by, value))
    )

def open_login_page(driver):
    driver.get(LOGIN_URL)

def check_password_field(driver):
    # pronalazak kontrole
    password_input = wait_for(driver, By.ID, "password")
    # provera tipa
    password_type = password_input.get_attribute("type")
    assert password_type == "password"

def fill_login_form(driver, username, password):
    username_input = wait_for(
        driver, By.ID, "username"
    )
    password_input = wait_for(
        driver, By.ID, "password"
    )
    # praznimo tekst polja
    username_input.clear()
    password_input.clear()

    username_input.send_keys(username)
    password_input.send_keys(password)

def submit_login_form(driver):
    submit_button = wait_for(driver, By.ID, "submit")
    submit_button.click()

def check_login_result_general(driver):
    # provera rezultata nakon submit-a
    current_url = driver.current_url
    if "logged-in-successfully" in current_url:
        naslov = wait_for(driver, By.TAG_NAME, "h1")
        assert "Logged In Successfully" == naslov.text.strip()
    else:
        error_msg = wait_for(driver, By.ID, "error")
        assert error_msg.is_displayed()

def check_login_positive_result(driver):
 # provera rezultata nakon submit-a
    current_url = driver.current_url
    assert "logged-in-successfully" in current_url
    naslov = wait_for(driver, By.TAG_NAME, "h1")
    assert "Logged In Successfully" == naslov.text.strip()

def check_login_negative_result(driver):
    error_msg = wait_for(driver, By.ID, "error")
    assert error_msg.is_displayed()
# Provera test slucajeva
# TC 1 - Uspesan login
  # 1. Dolazak na tranicu login
  # 2. provera tipa za tekst polje password
  # 3. popunjavanje polja ispravnim podacima - student i Password123
  # 4. klik na taster submit
  # 5. Provera url-a
  # 6. Provera naslova stranice
# TC 2 - Neuspesan login - neispravni kredencijali

def test_successful_login():
    driver = create_driver()
    open_login_page(driver)
    check_password_field(driver)
    fill_login_form(driver, "student", "Password123")
    submit_login_form(driver)
    check_login_positive_result(driver)
    time.sleep(5)
    driver.quit()

def test_login_negative_case():
    driver = create_driver()
    open_login_page(driver)
    check_password_field(driver)
    fill_login_form(driver, "abc", "123")
    submit_login_form(driver)
    check_login_negative_result(driver)
    time.sleep(5)
    driver.quit()

# setup - kreiranje drivera
# teardown - zatvaranje drivera
test_successful_login()
test_login_negative_case()