import unittest
from Health import Health

class SimpleTest(unittest.TestCase):
    def test_1(self):
        gender = 'male'
        height = 175
        expected = 73.3
        result = Health.calculate_ideal_weight(gender, height)

        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()