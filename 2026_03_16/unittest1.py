# Funkcija izracunavanja cene sa popustom
def cena_sa_popustom(cena, popust):
    izracunata_cena = cena - cena * popust / 100
    return izracunata_cena

rezultat = cena_sa_popustom(1000, 10)
print(rezultat)
######################################################################
def test_cena_sa_popustom(): 
    cena = 1000
    popust = 10
    ocekivano = 900.0

    dobijeno = cena_sa_popustom(cena, popust)
    print(ocekivano == dobijeno)

test_cena_sa_popustom() # Pokretanje Unit testova
###################################################################
def  login(user_name, password):
    # Dobavljam username iz baze
    # Dobavljam password iz baze
    if user_name == "admin" and password == "1234":
        return True
    
    return False
####################################################################################
# Proverava login sa ispravnim podacima
def test_ispravni_podaci():
    # Given
    kor_ime = "admin"
    sifra = "1234"
    # When
    rezultat_logovanja = login(kor_ime, sifra)
    # Then
    print(rezultat_logovanja == True)

test_ispravni_podaci()
############################################################################
# Provera login sa neispravnim podacima
def test_neispravni_podaci():
    kor_ime = "dadasgs"
    sifra = "4252"

    rezultat_logovanja = login(kor_ime, sifra)
    print(rezultat_logovanja == False)

test_neispravni_podaci()
#########################################################################
def deljenje(a, b):
    if b == 0:
        return "Nije dozvoljeno deljenje sa nulom"
    return f"Rezultat deljenja je: {a / b}"

print(deljenje(4, 2))

#################################################################################
godine = int(input("Unesite godine: "))

if godine >= 18 and godine <= 65:
    print("Dozvoljen pristup.")
else:
    print("Pristup nije dozvoljen!")

#########################################################################
def besplatna_dostava(premium_korisnik, iznos):
    if premium_korisnik and iznos > 5000:
        return True # print("Besplatna dostava")
    else:
        return False # print("Dostava se naplacuje")

ocekivano = False
dobijeno = besplatna_dostava(False, 4000)
print(ocekivano == dobijeno)

ocekivano = False
dobijeno = besplatna_dostava(True, 4000)
print(ocekivano == dobijeno)

ocekivano = False
dobijeno = besplatna_dostava(False, 5500)
print(ocekivano == dobijeno)

ocekivano = True
dobijeno = besplatna_dostava(True, 5500)
print(ocekivano == dobijeno)