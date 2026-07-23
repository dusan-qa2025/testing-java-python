poruke = ["Zdravo", "Hello", "Hallo"]
print(poruke[0])

poruke1 = {"sr":"Zdravo", "en":"Hello", "de":"Hallo"}
print(poruke1["sr"])
poruke1["sr"] = "Dobar dan"
print(poruke1)

poruke2 = {}
# Temperatura, Grad, Padavine da/ne

vremenska_prognoza = {"temperature":10, "city":"Beograd", "padavine":True}
# print(f"Temperatura: {vremenska_prognoza["temperatura"]}")
# print(f"Grad: {vremenska_prognoza["grad"]}")
# print(f"Padavine: {vremenska_prognoza["padavine"]}")

for kljuc, vrednost in vremenska_prognoza.items():
    print(kljuc, vrednost)

dogovoreni_kljucevi = ["temperatura", "grad", "padavine"]
for kljuc in dogovoreni_kljucevi:
    if kljuc in vremenska_prognoza:
        print(f"Kljuc {kljuc} je OK")
    else:
        print(f"Kljuc {kljuc} nije pronadjen!!!")


proizvod = {
    "naziv": "Patike", # string
    "cena": { # recnik
        "vrednost":200, 
        "valuta":"EUR"
        }, 
    "slike":["slika1.png", "slika2.png"] # lista
}
print(proizvod["naziv"])
informacije_o_ceni = proizvod["cena"]
print(informacije_o_ceni)
print(informacije_o_ceni["vrednost"])
print(informacije_o_ceni["valuta"])
lista_slika = proizvod["slike"]
print(lista_slika)
for slika in lista_slika:
    print(f"Slika: {slika}")

proizvodi = [
    {
    "naziv": "Patike", # string
    "cena": { # recnik
        "vrednost":200, 
        "valuta":"EUR"
        }, 
    "slike":["slika1.png", "slika2.png"] # lista
},
{
    "naziv": "Majica", # string
    "cena": { # recnik
        "vrednost":20, 
        "valuta":"EUR"
        }, 
    "slike":["slika3.png", "slika4.png"] # lista
}
]
print(len(proizvodi))
for proizvod in proizvodi:
    cena = proizvod["cena"] # recnik vezan za kljuc cena
    vrednost_cene = cena["vrednost"]
    valuta = cena["valuta"]
    print(f"Naziv: {proizvod["naziv"]}\nCena: {vrednost_cene} {valuta}")
    print("_____________________")

kurs = {
    "naziv":"Intro to Software Development",
    "trajanje":60, 
    "lekcije": [
         "Uvod u programiranje", 
         "Jira", 
         "Git"
         ]
    }
# print(kurs["naziv"])
# print(kurs["trajanje"])
# lekcije = kurs["lekcije"]
# for lekcija in lekcije:
#     print(lekcija)

obavezni_kljucevi_za_kurs = ["naziv", "trajanje", "lekcije"]
for kljuc in obavezni_kljucevi_za_kurs:
    # TRUE ili FALSE
      # not TRUE -> FALSE
      # not FALSE -> TRUE
    if not kljuc in kurs:
       print(f"Nedostaje obavezan kljuc: {kljuc}")

skup = {"Python", "QA", "Mobilno programiranje"}
skup.add("Web programiranje")
print(skup)
skup.remove("Web programiranje")
for element in skup:
    print(element)