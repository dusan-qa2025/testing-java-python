from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# otvorite veb-pregledač
driver = webdriver.Chrome()
 
# otvaramo željenu stranicu
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
 
# pronađite sve checkbox elemente u formi i ispišite njihov ukupan broj
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(f'Broj checkbox elemenata: {len(checkboxes)}')
 
# pronađite sve radio button elemente u formi i ispišite njihov ukupan broj
radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
print(f'Broj radio button elemenata: {len(radio_buttons)}')
 
# Sacekaj 5 sekundi da se ucita stranica nakon prijave
time.sleep(5)

# zatvorite pregledač
driver.quit()