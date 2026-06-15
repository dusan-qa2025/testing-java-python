from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")

user_text_field = driver.find_element(By.ID, "user-name")
user_text_field.send_keys("standard_user")

password_text_field = driver.find_element(By.ID, "password")
password_text_field.send_keys("sercret_cause")

driver.find_element(By.ID, "login-button").click()

title = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "title"))
)

assert title == "Products"

time.sleep(5)
driver.quit()

