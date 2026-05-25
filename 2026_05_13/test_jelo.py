import unittest
from jelo import Jelo
from unittest import TestCase

class TestJelo(TestCase):
    @classmethod
    def setUpClass(cls):
        print("PRE SVIH TESTOVA")

    @classmethod
    def tearDownClass(cls):
        print("NAKON SVAKOG TESTA")
        
    def setUp(self):
        print("JA SAM PRE SVAKOG TESTA - SETUP")
        self.jelo = Jelo("Pizza", 800)

    def tearDown(self):
        print("JA SAM NAKON SVAKOG TESTA - TEARDOWN")

    def test_promeni_cenu(self):

        print("TEST 1")

        self.jelo.promeni_cenu(900) 
        self.assertEqual(self.jelo.cena, 900) 

    def test_dodaj_porez(self):

        print("TEST 2")

        self.jelo.dodaj_porez(20)
        self.assertEqual(self.jelo.cena, 1200)

    def test_porez_nula(self):

        print("TEST 3")
        
        self.jelo.dodaj_porez(0)
        self.assertEqual(self.jelo.cena, 1000)

if __name__ == "__main__":
    unittest.main()
