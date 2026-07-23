import requests
from bs4 import BeautifulSoup

response = requests.get("https://example.com")
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
naslov = soup.find("h1")
print(naslov.text)

link = soup.find("a")
print(link.text)
print(link.get("href"))
ocekivani_link = "https://iana.org/domains/example"
