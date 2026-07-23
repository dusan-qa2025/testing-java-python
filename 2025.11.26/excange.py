# Vezba broj 1 

eur = 1.3
usd = 1.1
val = float(input("Enter value: ")) # npr. 130
total_euro = val / eur
total_dollars = val / usd

# Ispis formatiran na dve decimale
print("Total_Euro: %.2f" % total_euro)
print("Total_Dollars: %.2f" % total_dollars)

# Alternativno, sa f-stringovima:
# print(f"Total Euro: {total_euro:.2f}")
# print(f"Total Dollars: {total_dollars:.2f}")

print(f"Total Euro: {total_euro:.2f}")
print(f"Total Dollars: {total_dollars:.2f}")



# Vezba broj 2

import random
korisnikov_broj = 20
broj_racunara = random.randint(0, 20)
print("Pogodak: ", korisnikov_broj == broj_racunara)
print(f"Korisnik: {korisnikov_broj}, Racunar: {broj_racunara} ")


# Vezba broj 3 

starost_igraca = 15
allowed_age = 13

age = int(input("Unesi_svoje_godine: "))
allowed = age >= allowed_age
print("Allowed - ", allowed)


