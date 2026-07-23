#kafe = ["nes", "esspreso", "cappuccino"]

#for coffee in kafe:
 #   print(coffee)

#kafe.remove("nes")
#print(kafe)

kafe = open("kafe.txt", "a+")
#print(kafe)
#print(kafe.readlines())

proizvod = kafe.readline()
kafe.seek(0) # Vraca kursor na pocetku
print(proizvod)
#podaci = proizvod.strip().split(",")
#print(podaci)
#print("Proizvod:", podaci[0])
#print("Cena:", podaci[1])

svi_proizvodi = kafe.readlines()
print(svi_proizvodi)

for proizvod in svi_proizvodi:
    podaci = proizvod.strip().split(",")
    print(f"Proizvod: {podaci[0]}")
    print(f"Cena: {podaci[1]} RSD")
    print()

kafe.write("\ntea,150\n")
    