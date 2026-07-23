from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
 
import time
def test_google():
    # instanciramo Chrome pregledač
    driver = Chrome()
 
    # Otvaranje Google pretrage koristeći Chrome, slanjem GET zahteva
    driver.get("https://www.google.com/")
 
    # Pronalaženje polja za pretragu i unos ključnih reči "Selenium Python"
    # tražimo na HTML dokumentu polje koje ima name="q"
    search_field = driver.find_element(By.NAME, "q")
    # u polje za pretragu unosimo željeni tekst
    search_field.send_keys("Selenium Python")
    search_field.send_keys(Keys.RETURN)
 
    # Sačekaj 5 sekundi da se učitaju rezultati pretrage
    time.sleep(5)
 
    # Provera da li se "Selenium with Python" pojavljuje u rezultatima pretrage
    assert ("Selenium with Python" in driver.page_source)
 
    # Zatvaranje pregledača
    driver.quit()