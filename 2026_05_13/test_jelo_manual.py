import jelo as j
from jelo import Jelo


def test_promeni_cenu():
    
    # Given / Arrange
    pizza = Jelo("Pizza", 500)
    print("Pocetna cena:", pizza.cena)

    # When / Act 
    pizza.promeni_cenu(900)

    # Then / Assert
    assert pizza.cena == 900

def test_dodaj_porez():

    # Given / Arrange
    jelo = Jelo("Pasta", 1000)

    # When / Act
    jelo.dodaj_porez(20)

    # Then / Assert
    assert jelo.cena == 1200
    

test_promeni_cenu()
test_dodaj_porez()
