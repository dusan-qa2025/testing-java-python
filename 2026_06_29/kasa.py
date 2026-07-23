import time
import threading


stanje_u_kasi = 0

kasa_lock = threading.Lock()

def dodaj_u_kasu(iznos):
    global stanje_u_kasi

    #kasa_lock.acquire()
    with kasa_lock:
        # citanje trenutnog stanja u kasi
        trenutno_stanje = stanje_u_kasi
        time.sleep(0.001)
        # upis novog stanja u kasi
        stanje_u_kasi = trenutno_stanje + iznos
    #kasa_lock.release()
    
niti = []
for i in range(100):
    nit = threading.Thread(target=dodaj_u_kasu, args=(10,))
    niti.append(nit)
    nit.start()

for nit in niti:
    nit.join()



print("Ocekivano stanje u kasi:1000")
print(f"Stvarno stanje u kasi:{stanje_u_kasi}")