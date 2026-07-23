moji_oglasi = []

oglas1 = {
    "id": 123,
    "naziv": "Patike",
    "cena": 150,
    "opis": "Patike na prodaju"
}

moji_oglasi.append(oglas1)

oglas2 = {
    "id": 543,
    "naziv": "Jakna",
    "cena": -50,
    "opis": "Jakna na prodaju"
}
moji_oglasi.append(oglas2)

print(moji_oglasi)
# Utvrditi koji od oglasa ima negativnu cenu
for oglas in moji_oglasi:
    print(f"Naziv: {oglas["naziv"]}")
    print(f"Cena: {oglas["cena"]}")
    print(f"Opis: {oglas["opis"]}")

    cena = oglas["cena"]
    if cena < 0:
        print(f"!!! Oglas sa id-em {oglas["id"]} ima negativnu cenu. !!!")