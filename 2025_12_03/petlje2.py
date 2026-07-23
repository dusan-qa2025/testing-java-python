import random

tajmer = 5

while tajmer > 0:
    print(tajmer)
    tajmer -= 1

broj_pokusaja = 3

while broj_pokusaja > 0:
    print("Saljem zahtev za podatke")
    podaci = "Dobijeni podaci"
    if podaci != "":
        print("Napustam petlju")
        break
    else:
        broj_pokusaja -= 1

# stampati samo parne brojeve - simulacija continue
for broj in range(1,10):
    if broj % 2 != 0:
        continue
    print(broj)

gorivo = 40
#potrosnja = 5

while gorivo > 0:
    print("Voznja u toku")
    gorivo -= random.randint(6,15)

# unesi x za zavrsetak, pritisni enter "" za prikaz rezultata
suma = 0
while True:
    vrednost = input("Unesite broj: ")

    if vrednost == "":
        print("Suma:", suma)
        suma = 0
    else:
        if vrednost == "x":
            print("Zavrsavam program")
            break
        else:
            if vrednost.isnumeric():
                suma += int(vrednost)
            else:
                print("Molimo unesite samo brojeve.")