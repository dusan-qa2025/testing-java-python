# stampati samo parne brojeve
for broj in range(10):
    if broj % 2 != 0:
        continue
    else:
        print(broj)

gorivo = 40
#potrosnnja = 5

while gorivo > 0:
    print("Voznja u toku")
    

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




