from jelo import Jelo
import pytest

@pytest.fixture
def pizza():
    return Jelo("Pizza", 800)

# cena, porez, ocekivano
@pytest.mark.parametrize("cena, porez, ocekivano", [(1000, 20, 1200)])
def test_dodaj_porez(cena, porez, ocekivano):
    jelo = Jelo("Pizza", cena)
    jelo.dodaj_porez(porez)
    assert jelo.cena == ocekivano


def test_promeni_cenu(pizza):
    pizza.promeni_cenu(900)
    assert pizza.cena == 900

