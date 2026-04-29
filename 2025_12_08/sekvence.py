# BROJEVI = RANGE(1,5) # 1234
for broj in range ( 1,5):
    print(broj)
#        01234
poruka = "Hello"
broj_karaktera = len(poruka)
print(broj_karaktera)
for x in range (0,5):
    print(poruka[x])
# print(poruka[0])
# print(poruka[1])
# print(poruka[2])
# print(poruka[3])
# print(poruka[4])


for slovo in poruka:
    print(slovo)


poruka = "Zdravo, kako ste? "
print(len(poruka))

poruka = "Hello World"
print(poruka.upper())
print(poruka.lower())
print(poruka.capitalize())


brojevi = [3 , 10 , 12 ,2 ,7]
print(brojevi[0])
for broj in brojevi:
    print(broj)
for x in range(0, len(brojevi)):
    print(brojevi[x])

korisnicka_imena = ("gost54", "petar123", "jovana555")
for x in range(len(korisnicka_imena)):
    print(korisnicka_imena[x])


korisnici = [ "petar" "ana" "petra"]
for i in range(len(korisnici))

for indeks, vrednost in enumerate(korisnici):
    print(f"Indeks: {indeks}, Vrednost: {vrednost}")