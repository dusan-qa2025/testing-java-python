# igrac, ukupan broj poena, ukupan broj utakmica
# lista igraca
igraci = [
{"prezime": "Jokic", "poeni":100, "ukupan_broj_utakmica": 10},
{"prezime":"Gordon", "poeni": 20, "ukupan_broj_utakmica": 11},
{"prezime":"Saric", "poeni": 50, "ukupan_broj_utakmica":12}
]

def izracunaj_prosek_poena(broj_poena, ukupno_utakmica):
    rezultat = broj_poena / ukupno_utakmica
    return rezultat

for igrac in igraci:
    print(f"Igrac: {igrac["prezime"]}")
    print(izracunaj_prosek_poena(igrac["poeni"], igrac["ukupan_broj_utakmica"]))


# Testiranje funkcije za izracunavanje proseka
# Test podaci
broj_poena_test = 50
ukupno_utakmica_test = 10
ocekivano = 5

dobijeno = izracunaj_prosek_poena(broj_poena_test, ukupno_utakmica_test)
print(ocekivano == dobijeno)

# izdvajanje testa u zasaebnu funkciju
def test_proseka_poena(broj_poena, ukupno_utakmica, ocekivano):
    dobijeno = izracunaj_prosek_poena(broj_poena, ukupno_utakmica)
    print(ocekivano == dobijeno)

    test_prosao = ocekivano == dobijeno
    return test_prosao