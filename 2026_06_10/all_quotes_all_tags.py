from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://quotes.toscrape.com/")

quotes = driver.find_elements(By.CLASS_NAME, "quote") # svi citati

all_tag_names = [] # svi tagovi - lista

# all_tag_names = set() # skup - ne ponavljaju se vrednosti
# all_tag_names.add(...) - dodavanje elementa u skup

for quote in quotes:
    # nalazimo se u jednom citatu u petlji
    tags = quote.find_elements(By.CLASS_NAME, "tag")
    for tag in tags:
        all_tag_names.append(tag.text) # dodajemo u listu svih tagova

for tag_name in all_tag_names:
    driver.get("https://quotes.toscrape.com/")
    tag_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, tag_name))
    )
    tag_link.click()

    heading = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h3"))
    )

    assert heading.text == f"Viewing tag: {tag_name}"

time.sleep(5)
driver.quit()