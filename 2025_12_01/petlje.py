import time
for  i in range(5):
    print("Hello", i)
    print("******")

print("Prva sledeca linija")

pocetna_godina = 2010
krajnja_godina = 2025

for godina in range(pocetna_godina, krajnja_godina):
     print("*********Allowed years*********")

broj = 5
print("1\t2\t3")
print(20*"dobro dosao")
for x in range(1, broj +1):
    print(f"{x*1}\t{x*2}\t{x*3}")


# iscrtati kvadrat 
###
###
###
for x in range(3):
     for y  in range (3):
        print("#", end="" )



visina = 5
sirina = 10

for x in range(visina):
    for y in range(sirina):
        if x == 0 or x == 4 or y == 0 or y == 9:
             print("#", end="")
        else:
            print(" ", end=" ")
    print()
    




cilj = 20
trenutna_pozicija = 0

for x in range(cilj):
    print(trenutna_pozicija * " " + "#", end="\r")
    print( "#", end="\r")
    trenutna_pozicija += 1
    time.sleep(1)



