import unittest
from test_jelo import TestJelo

suite = unittest.TestSuite()
suite.addTest(TestJelo("test_dodaj_porez"))
suite.addTest(TestJelo("test_porez_nula"))

runner = unittest.TextTestRunner()
runner.run(suite)
