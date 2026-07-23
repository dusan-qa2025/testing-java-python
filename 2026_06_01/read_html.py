from bs4 import BeautifulSoup

with open("index.html", "r", encoding="utf-8") as fajl:
    sadrzaj = fajl.read()

# pronadji naslov na strani (h1)
soup = BeautifulSoup(sadrzaj, "html.parser")
# .....
naslov = soup.find("h1")
ocekivano = "Pet Shop"
dobijeno = naslov.text
assert ocekivano == dobijeno

stavke_liste = soup.find_all("li")
print(stavke_liste)

print(len(stavke_liste))
for stavka in stavke_liste:
    print(stavka.text)

link = soup.find("a")
print(link)

putanja = link.get("href")
print(putanja)

ponuda = soup.find_all("ul")
print(ponuda)

for element in ponuda:
    if element.get("id") == "ponuda":
        print(element)
