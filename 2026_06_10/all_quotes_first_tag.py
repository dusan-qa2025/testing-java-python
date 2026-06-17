from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://quotes.toscrape.com/")

quotes = driver.find_elements(By.CLASS_NAME, "quote")

first_tags_from_quotes = [] # pokupim prve tagove iz svakog

for quote in quotes:
    # trazim prvi tag
    first_tag = quote.find_element(By.CLASS_NAME, "tag")
    first_tags_from_quotes.append(first_tag.text)

for tag in first_tags_from_quotes:
    driver.get("https://quotes.toscrape.com/")
    tag_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, tag))
    )
    tag_link.click()

    heading = wait.until(
        EC.visibility_of_element_located((By.TAG_NAME, "h3"))
    )

    assert heading.text == f"Viewing tag: {tag}"

time.sleep(5)
driver.quit()