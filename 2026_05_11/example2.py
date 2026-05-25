def prikazi_rezultat_testa(naziv_testa, dobijeno, ocekivano):
    print("Test:", naziv_testa)
    print("Dobijeno:", dobijeno)
    print("Ocekivano:", ocekivano)
    print("Test prosao:", ocekivano == dobijeno)
    print("#####################################################")

def validiraj_password(password):
    return len(password)>=8

# Password je validan ako ima 8 karaktera
def test_validan_password():
    ocekivano = True
    dobijeno = validiraj_password("12345678")
    prikazi_rezultat_testa("Validan password", dobijeno, ocekivano)


def test_kraci_password():
    ocekivano = False
    dobijeno = validiraj_password("1234567")
    prikazi_rezultat_testa("Kraci password od zahtevanog", dobijeno, ocekivano)

def test_prazan_password():
    ocekivano = False
    dobijeno = validiraj_password("")
    prikazi_rezultat_testa("Prazan password", dobijeno, ocekivano)

 
test_kraci_password()
test_validan_password()
test_prazan_password()