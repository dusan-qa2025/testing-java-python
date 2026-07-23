import unittest
import math

class TestMathFuncs(unittest.TestCase):

    def test_fabs(self):
        self.assertEqual(math.fabs(-6), 6)

    def test_isfinite(self):
        self.assertTrue(math.isfinite(56))
        self.assertFalse(math.isfinite(math.inf))

    def test_floor(self):
        self.assertEqual(math.floor(6.6), 6)
        self.assertRaises(TypeError, math.floor, "hello")
        

if __name__ == '__main__':
    unittest.main()
    