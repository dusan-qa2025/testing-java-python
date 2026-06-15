from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
 
# Otvaranje Chrome pregledača
driver = webdriver.Chrome()
 
# Otvaranje stranice sa login formom
driver.get("http://example.com/login")
 
# Pronalaženje polja za unos korisničkog imena i unos korisničkog imena
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("moje_korisnicko_ime")
 
# Pronalaženje polja za unos lozinke i unos lozinke
password_field = driver.find_element(By.NAME,"password")
password_field.send_keys("moja_lozinka")
 
# Klik na dugme za prijavu
login_button = driver.find_element(By.NAME,"login")
login_button.click()
 
# Sacekaj 5 sekundi da se ucita stranica nakon prijave
time.sleep(5)
 
# Provera da li se poruka prikazuje na stranici nakon prijave
assert "Dobrodošli!" in driver.page_source
 
# Zatvaranje pregledača
driver.quit()