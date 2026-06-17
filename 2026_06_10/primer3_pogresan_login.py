from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")

user_text_field = driver.find_element(By.ID, "user-name")
user_text_field.send_keys("test") # pogresan user name

password_text_field = driver.find_element(By.ID, "password")
password_text_field.send_keys("1234") # pogresan password

driver.find_element(By.ID, "login-button").click()

error_message = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
)

print(error_message.text)
assert "Epic sadface: Username and password do not match any user in this service" == error_message.text.strip()

time.sleep(5)
driver.quit()