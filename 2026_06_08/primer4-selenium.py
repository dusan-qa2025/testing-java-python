from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/")

wait = WebDriverWait(driver, 10)

# pronadji citate
# quotes = driver.find_elements(By.CLASS_NAME, "quote")
# for quote in quotes:
#     text = quote.find_element(By.CLASS_NAME, "text").text
#     author = quote.find_element(By.CLASS_NAME, "author").text

#     print(text , author)
#     print("***********")

# Pronadji specifican tag (link)
deep_thoughts_tag = driver.find_element(By.LINK_TEXT, "deep-thoughts")
# print(deep_thoughts_tag)
time.sleep(2)
deep_thoughts_tag.click()

naslov = wait.until(
    EC.visibility_of_element_located((By.TAG_NAME, "h3"))
)

# naslov = driver.find_element(By.TAG_NAME, "h3")

ocekivani_naslov = "Viewing tag: deep-thoughts!"

if naslov.text == ocekivani_naslov:
    print("Test je prosao")
else:
    print("Test nije prosao")
    driver.save_screenshot("deep_thoughts_page.png")

time.sleep(15)

driver.quit()