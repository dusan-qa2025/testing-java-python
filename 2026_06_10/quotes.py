from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://quotes.toscrape.com/")

first_quote = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "quote"))
)

first_tag = first_quote.find_element(By.CLASS_NAME, "tag") # tag element

tag_name = first_tag.text # tekst na tagu

first_tag.click() # interakcija

heading = wait.until(
    EC.visibility_of_element_located((By.TAG_NAME, "h3"))
) # naslov na drugoj stranici

expected_heading = f"Viewing tag: {tag_name}"

assert heading.text == expected_heading

time.sleep(5)
driver.quit()