from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import getpass
from selenium.webdriver.common.keys import Keys

LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(LOGIN_URL)

wait = WebDriverWait(driver, 10)

username_input = wait.until(
    EC.visibility_of_element_located((By.ID, "username"))
)

password_input = wait.until(
    EC.visibility_of_element_located((By.ID, "password"))
)

password_type = password_input.get_attribute("type")
assert password_type == "password"

# usernname = input("Unesi username: ") - unos kroz konzolu
# password_text = getpass.getpass("Unesi passowrd: ") - sakriven password kroz unos

# unos
username_input.send_keys("student")
password_input.send_keys("Password123")

#lociranje tastera i klik
submit_button = wait.until(
    EC.visibility_of_element_located((By.ID, "submit"))
)

submit_button.click() # - klik na taster
# submit_button.send_keys(Keys.ENTER) - klik enter (moze i na tekst polje)


# https://practicetestautomation.com/practice-test-login/ - sa ove stranice
# https://practicetestautomation.com/logged-in-successfully/ - idemo na ovu adresu

# trenutni url
current_url = driver.current_url
if "logged-in-successfully" in current_url:
    naslov = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "Logged In Successfully" == naslov.text.strip()
else:
    print("Korisnik nije na ispravnom url-u ili je ostao na istoj strani")
    error_msg = wait.until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    assert error_msg.is_displayed() # da li se prikazuje

time.sleep(5)

driver.quit()