import unittest

import test_math_funcs as test_math
import test_string_funcs as test_string

suite = unittest.TestSuite()
suite.addTest(test_string.TestStringFuncs("test_upper"))
suite.addTest(test_math.TestMathFuncs("test_fabs"))
suite.addTest(test_math.TestMathFuncs("test_isfinite"))
suite.addTest(test_math.TestMathFuncs("test_floor"))
suite.addTest(test_string.TestStringFuncs("test_isupper"))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
