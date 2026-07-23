import threading
import time

kljuc_od_auta = threading.Lock()
dokumenta = threading.Lock()

def korisnik_1():
    print("Korisnik 1 uzima kljuc od auta")

    with kljuc_od_auta:
        time.sleep(1)
        print("Korisnik 1 pokusava da uzme dokumenta")
        # provera da li su dokumenta dobijena 
        dobila_dokumenta = dokumenta.acquire(timeout=2)
        if dobila_dokumenta:
            try:
                print("Korisnik 1 ima i kljuc i dokumenta")
            finally:
                print("Timeout")
                dokumenta.release()
        else:
            print("Korisnik odustaje")

def korisnik_2():
    print("Korisnik 2 uzima dokumenta")

    with dokumenta:
        time.sleep(1)
        print("Korisnik 2 pokusava da uzme kljuc")

        dobio_kljuc = kljuc_od_auta.acquire(timeout=2)

        if dobio_kljuc:
            try:
                print("Korisnik 2 ima i dokumenta i kljuc")
            finally:
                kljuc_od_auta.release()
        else:
            print("Nije dobio kljuc i odustaje")

korisnik_1_thread = threading.Thread(target=korisnik_1)
korisnik_2_thread = threading.Thread(target=korisnik_2)

korisnik_1_thread.start()
korisnik_2_thread.start()

korisnik_1_thread.join()
korisnik_2_thread.join()

print("Program zavrsen")