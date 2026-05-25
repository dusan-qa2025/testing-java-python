def saberi(a, b):
    return a+b

def test_saberi_dva_pozitivna_broja():
    ocekivano = 5
    dobijeno = saberi(2, 3)

    print("Test sabiranja 2 pozitivna broja")
    print("Ocekivano:", ocekivano)
    print("Dobijeno:", dobijeno)
    print("Test prosao:", ocekivano == dobijeno)

test_saberi_dva_pozitivna_broja()
