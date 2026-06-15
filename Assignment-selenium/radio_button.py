from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

radio_buttons = driver.find_elements(By.NAME, "my-radio")
print(len(radio_buttons))

radio_buttons[0].click()

if radio_buttons[0].is_selected() and not radio_buttons[1].is_selected():
    print("PASS - The first radio button is selected.")
else:
    print("FAIL -The first radio button is not selected correctly.")

radio_buttons[1].click()

if radio_buttons[1].is_selected() and not radio_buttons[0].is_selected():
    print("PASS - The second radio button is selected, the first is deselected.")
else:
    print("FAIL - radio buttons do not work properly.")


time.sleep(3)
driver.quit()

