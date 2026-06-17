from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

# podesavanje password managementa u browseru
options = Options()
prefs = {
    "credentials_enable_service":False,
    "profile.password_manager_enabled":False,
    "profile.password_manager_leak_detection":False
}
options.add_experimental_option("prefs", prefs)

# instanciranje drivera (browser - sa podesavanjima)
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 10)

driver.get("https://www.saucedemo.com/")

user_text_field = driver.find_element(By.ID, "user-name")
user_text_field.send_keys("standard_user") # ispravan user name

password_text_field = driver.find_element(By.ID, "password")
password_text_field.send_keys("secret_sauce") # ispravan password

driver.find_element(By.ID, "login-button").click() # login btn click

title = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "title"))
)

assert title.text == "Products"

time.sleep(5)
driver.quit()