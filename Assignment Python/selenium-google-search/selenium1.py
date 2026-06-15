from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
 
# Otvaranje Chrome pregledača
driver = Chrome()
#otvaramo veb-formu
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
 
#uzimamo title stranice
title = driver.title
print(title)
#implicitno čekanje od 2 sekunde dok se stranica ne učita
driver.implicitly_wait(2)
 
# tražimo element koji ima name=my-text
text_box = driver.find_element(By.NAME, "my-text")
# lociramo i button element na stranici
submit_button = driver.find_element(By.CSS_SELECTOR, "button")
# unosimo u tekstualno polje tekst "Selenium"
text_box.send_keys("Selenium")
# simuliramo klik na dugme
submit_button.click()
 
# lociramo element koji ima ID="message"
message = driver.find_element(By.ID, "message")
#uzimamo tekstualni sadržaj ovog elementa i ispisujemo ga korisniku
value = message.text
print(value)

time.sleep(5)
driver.quit()