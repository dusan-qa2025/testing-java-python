class Jelo:

    @classmethod
    def ispisi_naziv_restorana(cls):
        print("Naziv restorana je:...") # klasni metod za ceo tips

    def __init__(self, naziv, cena):
        self.naziv = naziv
        self.cena = cena
    
    def promeni_cenu(self, nova_cena):
        self.cena = nova_cena

    def dodaj_porez(self, procenat):
        self.cena = self.cena + (self.cena * procenat / 100)

Jelo.ispisi_naziv_restorana()

if __name__ == "__main__":  
    print("ABCD")
    