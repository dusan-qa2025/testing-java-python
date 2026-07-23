import time
import threading
import random

def korisnik_salje_zahtev(korisnik_id):
    print(f"Korisnik {korisnik_id} salje zahtev")

    vreme_cekanja = random.randint(1, 5)
    time.sleep(vreme_cekanja)

    print(f"Korisnik {korisnik_id} je dobio odgovor nakon {vreme_cekanja} sekundi")

# nit = threading.Thread(target=korisnik_salje_zahtev, args=(1,))
# nit1 = threading.Thread(target=korisnik_salje_zahtev, args=(2,))
# nit.start()
# nit1.start()

niti = []
for korisnik_id in range(1, 6):
    nit = threading.Thread(target=korisnik_salje_zahtev, args=(korisnik_id,))
    niti.append(nit)
    nit.start()

for nit in niti:
    nit.join()