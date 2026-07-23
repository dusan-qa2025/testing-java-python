broj = 10
#uvecavanje broja
broj = broj + 10
print(broj)

broj += 10
broj = broj * 2
broj *= 2

broj += 1

# povrsina kruga - r na kvadrat puta pi
# ** kvadrat * puta
pi = 3.14
r = float(input("Unesite vrednost za poluprecnik: "))
 # povrsina = r ** 2 * pi
 # print(povrsina)



import random
korisnikov_broj = 10
broj_od_racunara = random.randint(1, 10)
print("Pogodak:", korisnikov_broj == broj_od_racunara)
print(f"Korisnik: {korisnikov_broj}, Racunar: {broj_od_racunara} ")