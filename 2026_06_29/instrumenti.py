import time
import threading

def svirka(instrument, trajanje):
    print(f"Pocinjem svirku: {instrument}")
    time.sleep(trajanje)
    print(f"Zavrsavam svirku: {instrument}")

instrumenti = [
    ("gitara", 3),
    ("violina", 7),
    ("kahon", 5)
]

print("Koncert pocinje")
# svirka("gitara", 3)
# svirka("violina", 7)
# svirka("kahon", 5)
# gitara_thread = threading.Thread(target=svirka, args=("gitara", 3))
# violina_thread = threading.Thread(target=svirka, args=("violina", 7))
# kahon_thread = threading.Thread(target=svirka, args=("kahon", 5))

# gitara_thread.start()
# violina_thread.start()
# kahon_thread.start()

# gitara_thread.join()
# violina_thread.join()
# kahon_thread.join()

niti = []

for instrument, trajanje in instrumenti:
    nit = threading.Thread(target=svirka, args=(instrument, trajanje))
    niti.append(nit)

pocetak = time.time()
print(pocetak)

for nit in niti:
    nit.start()

for nit in niti:
    nit.join()

kraj = time.time()

ukupno_trajanje = kraj - pocetak
print(f"Ukupno trajanje koncerta: {ukupno_trajanje} sekundi")