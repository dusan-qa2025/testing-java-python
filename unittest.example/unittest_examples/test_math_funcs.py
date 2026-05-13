import unittest
import math


class TestMathFuncs(unittest.TestCase):

    def setUp(self):
        print("Hello from setUp!")
        self.addCleanup(self.cleanAllResources)

    def  tearDown(self):
        print("Hello from tearDown!")

    @classmethod
    def setUpClass(self):
        print("Hello from setUpClass!")
    
    @classmethod
    def tearDownClass(self):
        print("Hello from tearDownClass!")
        
    def test_fabs(self):
        self.assertEqual(math.fabs(-6), 6)

    def test_isfinite(self):
        self.assertTrue(math.isfinite(56))
        self.assertFalse(math.isfinite(math.inf))

    def test_floor(self):
        self.assertEqual(math.floor(6.6), 6)
        self.assertRaises(TypeError, math.floor, "hello")

    def cleanAllResources(self):
        # Resource cleaning
        print("Hello from cleanup!")

if __name__ == '__main__':
    unittest.main()
    

