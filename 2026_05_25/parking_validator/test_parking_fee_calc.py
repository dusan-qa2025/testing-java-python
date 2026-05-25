import unittest
from unittest import TestCase

from parking_fee_calc import ParkingfeeCalculator

class ParkingFeeCalculatorTest(unittest.TestCase):

    calculator = ParkingfeeCalculator()

    def setUp(self):
        self.calculator = ParkingfeeCalculator()

    def test_for_zone_a_valid_case(self):
        calculator = ParkingfeeCalculator()
        cena = self.calculator.calculate_fee("A", 2)
        self.assertEqual(200, cena)


    def test_for_zone_b_valid_case(self):
        calculator = ParkingfeeCalculator()
        cena = self.calculator.calculate_fee("B", 3)
        self.assertEqual(210, cena)

    def test_for_zone_c_valid_case(self):
        calculator = ParkingfeeCalculator()
        cena = self.calculator.calculate_fee("C", 4)
        self.assertEqual(200, cena)

    def test_invalid_hours(self):
        calculator = ParkingfeeCalculator()
        cena = self.calculator.calculate_fee("A", -1)
        self.assertEqual(0, cena)

    def test_invalid_negative_hours(self):
        cena = self.calculator.calculate_fee("A", -1)
        self.assertEqual(0, cena)

    def test_unknown_zone(self):
        calculator = ParkingfeeCalculator()
        cena = self.calculator.calculate_fee("X", 5)
        self.assertEqual(-1, cena)

if __name__ == "__main__":
    unittest.main()