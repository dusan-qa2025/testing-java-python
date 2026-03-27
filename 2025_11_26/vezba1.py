# definisanje telefona - iz vezbe
proizvodjac = "Samsung" # string tip
model = "S25"  # string tip
cena = 800
url_do_slike = "samsung_slika.jpg"

'''
Proizvodjac: Samsung
Model: S25
Cena: 800$
'''

# print("Proizvodjac:",proizvodjac, "Model:",model, "Cena:",cena)
print(f"Proizvodjac: \t{proizvodjac}\nModel:\t{model}\nCena:\t{cena}$")
# \t - tab
# \n - novi red
print(cena + 50)
print(cena)

cena = cena + 50
print(cena)

cena = cena - 30
print(cena)

popust = 0.2
umanjenje = cena * 0.2
cena = cena - umanjenje
print(cena)

cena_bez_popusta = 800
print(int(cena_bez_popusta / 2)) # float -> int

# deljenje bez ostatka //
print(25 // 2)

# stepenovanje **
print(8**3)
print(2**2)

# celobrojni ostatak pri deljenju %
print(10 % 2)
print(10 % 3) # 3 * 3 = 9 + 1 = 10

# Trazimo od korisnika broj i proveravamo da li je paran broj
uneti_broj = int(input("Unesite broj: "))
ostatak_pri_deljenju_sa_dva = uneti_broj % 2 
broj_je_paran = ostatak_pri_deljenju_sa_dva == 0 # True / False
print(broj_je_paran)

# Test plan
# test_broj 15
# ocekivano - nije paran - Rezultat: False
ocekivano = False
print("Test je prosao:", broj_je_paran == ocekivano)

# test slucaj za parne 
# test_broj 16
# ocekivano - da je paran - Rezultat: True
ocekivano_2 = True
print("Test je prosao: ", broj_je_paran == ocekivano_2)

# Opis buga
# Provera da li je broj paran
# Reprodukcija buga:
# 1. Unet je broj 16
# 2. Klik na enter
# Dobijeno: False - da broj nije paran
# Ocekivano: True - broj je paran

# Proveravamo oba slucaja - Bug ispravljen