import threading
import time

def ucitaj_podatke(naziv):
    print(f"Pocinjem ucitavanje: {naziv}")
    time.sleep(3)
    print(f"Zavrsavam ucitavanje: {naziv}")

print("Aplikacija se pokrece")
#ucitaj_podatke("korisnik")
#ucitaj_podatke("proizvodi")
#ucitaj_podatke("notifikacije")

nit1 = threading.Thread(target=ucitaj_podatke, args=("korisnik",))
nit2 = threading.Thread(target=ucitaj_podatke, args=("proizvodi",))
nit3 = threading.Thread(target=ucitaj_podatke, args=("notifikacije",))

nit1.start()
nit2.start()
nit3.start()

nit1.join()
nit2.join()
nit3.join()

print("Aplikacija se zavrsava")