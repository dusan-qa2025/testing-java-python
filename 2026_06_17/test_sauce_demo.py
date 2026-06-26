import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_URL = "https://www.saucedemo.com/"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

def test_full_checkout_flow():
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled":False,
        "profile.password_manager_leak_detection": False,
        "profile.password_manager_leak_detection_enabled": False
    }
    options.add_experimental_option("prefs", prefs)

    browser = webdriver.Chrome(options=options)
    browser.maximize_window()

    browser.get(BASE_URL)

    wait = WebDriverWait(browser, 10)
    # LOGIN - prebaciti u pomocnu funkciju def login(driver):
    username_input = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    username_input.send_keys(USERNAME)

    password_input = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password_input.send_keys(PASSWORD)

    login_button = wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )

    login_button.click()

    # PROVERA DA SMO NA PRODUCTS STRANI
    page_title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert page_title.text == "Products"

    # LOCIRANJE PROIZVODA
    first_product = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item"))
    )

    product_name = first_product.find_element(By.CLASS_NAME, "inventory_item_name")
    product_price = first_product.find_element(By.CLASS_NAME, "inventory_item_price")

    assert product_name.text.strip() == "Sauce Labs Backpack"
    assert product_price.text.strip() == "$29.99"

    # KLIK NA DODAJ PROIZVOD
    add_to_cart_button = first_product.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    )
    add_to_cart_button.click()

    # PROVERA BADGE-a NA KORPI
    cart_badge = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert cart_badge.text == "1"

    # OTVARANJE KORPE
    cart_link = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_link"))
    )
    cart_link.click()

    # PROVERA DA LI SMO U KORPI
    cart_title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert cart_title.text.strip() == "Your Cart"

    # PROVERA PROIZVODA U KORPI
    cart_product_name = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )
    cart_product_price = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_price"))
    )
    assert cart_product_name.text.strip() == "Sauce Labs Backpack"
    assert cart_product_price.text.strip() == "$29.99"

    # KLIK NA CHECKOUT
    checkout_button = wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()

    # PROVERA STRANE ZA CHECK OUT
    checkout_title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert checkout_title.text.strip() == "Checkout: Your Information"

    # POPUNJAVANJE CHECKOUT FORME - def fill_checkout_form(driver)
    first_name_input = wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )
    first_name_input.send_keys("Dusan")

    last_name_input = wait.until(
        EC.visibility_of_element_located((By.ID, "last-name"))
    )
    last_name_input.send_keys("Milosavljevic")

    postal_code_input = wait.until(
        EC.visibility_of_element_located((By.ID, "postal-code"))
    )
    postal_code_input.send_keys("17510")

    continue_button = wait.until(
        EC.element_to_be_clickable((By.ID, "continue"))
    )
    continue_button.click()

    # PROVERA OVERVIEW STRANICE
    overview_title = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )
    assert overview_title.text.strip() == "Checkout: Overview"

    # zavrsetak kupovine def finish_order(driver)
    finish_button = wait.until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )
    finish_button.click()

    complete_header = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert complete_header.text.strip() == "Thank you for your order!"

    time.sleep(5)
    browser.quit()