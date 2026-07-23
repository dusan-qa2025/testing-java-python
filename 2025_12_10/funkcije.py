
def ispisi_poruku(korisnicko_ime="gost"): # funkcija sa opcionim parametrom
    print(f"Zdravo {korisnicko_ime}!!!")

# print(korisnicko_ime) ne postoji izvan tela funkcije
ispisi_poruku("Admin")
ispisi_poruku()

# def saberi(prvi_sabirak=0, drugi_sabirak=0):
#     print(prvi_sabirak + drugi_sabirak)

# # saberi(prvi_sabirak=10, drugi_sabirak=20)
# saberi()

def dodaj_oglas(naziv, cena, dodatne_informacije=""):
    print(f"Naziv: {naziv}")
    print(f"Cena: {cena}")
    if dodatne_informacije != "":
        print(f"Dodatne info: {dodatne_informacije}")

dodaj_oglas("Patike", 200)
dodaj_oglas("Automobil", 5000, "U odlicnom stanju")
dodaj_oglas(cena=500, naziv="Slusalice", dodatne_informacije="Informacije....")

brojevi = [5, 3, 4]
broj_clanova = len(brojevi)
print(broj_clanova)

def pomnozi(broj1, broj2):
    rezultat = broj1 * broj2
    return rezultat
    # print("Pozdrav iz funkcije za mnozenje") ovo se nikad ne izvrsava jer je nakon return-a

rezultat_mnozenja = pomnozi(5, 3)
print(rezultat_mnozenja)