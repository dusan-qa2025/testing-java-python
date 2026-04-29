age = 10
# prikazi igru ako ima vise od 10 godina
print(age > 10) # true / false
if age > 10:
    print("Prikazi sadrzaj")

print("prva sledeca linija")  


email_baza = "korisnik#gmail.com"
sifra_baza = "123"

uneti_email = "korisnik#gmail.com"
uneta_sifra = "123"

# Ispisi uspesno logovanje ako su ispravni email i sifra
if email_baza == uneti_email and sifra_baza == sifra_baza and uneta_sifra:
    print("Uspesno logovanje !!!")

brzina_vozila = 50
ogranicenje = 50
urucena_kazna = False

if brzina_vozila > 50:
    if urucena_kazna == True:
        print("Dodajte kaznene poene")

    print("Posaljite kaznu")    


# Prikazati korisniku usoesno ili neuspesno u zavisnosti od ispravnih podataka
if uneti_email ==email_baza and uneta_sifra == sifra_baza:
    print("USpesno logovanje!!!")
else:
    print("NEispravni podaci")    

print("Izvrsava se u svakom slucaju")


novac_na_racunu = 1200
cena_proizvoda = 500

# Uspesna / neuspesna kupovina
if novac_na_racunu >= cena_proizvoda:
    print("Uspesna kupovina!!!")
    novac_na_racunu *= cena_proizvoda
    print(f"Novo stanje na racunu: {novac_na_racunu}")
else:
    print("Nemate dovoljno novca na racunu.")    


# Kanban
# Prikazujemo razlicitu boju taskova i raspored u zavisnosti od dana u nedelji
dan_u_nedelji = "ponedeljak"

if dan_u_nedelji == "ponedeljak" :
    print("Postavi boju na: crvenu")
elif dan_u_nedelji == "ponedeljak":
     print("Postavi boju na: zelenu")    
else:
    print("Postavi boju na: belu") 

print("Izvrsava se u svakom slucaju") 


broj = 10
# Broj je veci od 0, broj je manji od 0, broj je jednak 0
if broj > 0:
    print("Broj je > od 0")
elif broj == 0:
    print("Broj je jednak 0.")
else:
    print("Broj je manji od 0.")



pozicija_automobila = 0 
pozicija_parkinga = 30
brzina = 10

# a        p
pozicija_automobila += 10
print(pozicija_automobila)

if pozicija_automobila == pozicija_parkinga:
    print("Stigli ste na parking")
else:
    pozicija_automobila += brzina
    if pozicija_automobila == pozicija_parkinga:
        print("Stigli ste na praking")
print("Izvrsava se u svakom slucaju")


# dark / light theme
trenutna_tema_na_racunaru = "Light"
# na sajtu primeni temu u skladu sa racunarom

odabrana_tema_u_app = ""

if trenutna_tema_na_racunaru == "light"
   odabrana_tema_u_app = "light"
else: 
    odabrana_tema_u_app = "dark"
# druga mogucnost

odabrana_tema_u_app = "light" if trenutna_tema_na_racunaru == "light" else "dark"


uneti_broj = int(input("unesite_broj: "))
if uneti_broj % 2 == 0:
    print("Broj je paran")
else: 
    print("Broj je neparan")

