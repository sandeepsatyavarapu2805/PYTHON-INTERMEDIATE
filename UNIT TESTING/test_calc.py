import unittest, calc

class TestCalc(unittest.TestCase):
    
    # we need to add test at the start so it knows what to run for tests
    def test_add(self):
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)

    def test_sub(self):
        self.assertEqual(calc.subtract(10,5), 5)
        self.assertEqual(calc.subtract(-1,1), -2)
        self.assertEqual(calc.subtract(-1,-1), 0)

    def test_mul(self):
        self.assertEqual(calc.multiply(10,5), 50)
        self.assertEqual(calc.multiply(-1,1), -1)
        self.assertEqual(calc.multiply(-1,-1), 1)

    def test_div(self):
        self.assertEqual(calc.divide(10,5), 2)
        self.assertEqual(calc.divide(-1,1), -1)
        self.assertEqual(calc.divide(-1,-1), 1)
        self.assertEqual(calc.divide(5,2), 2.5)

        # self.assertRaises(ValueError, calc.divide, 10, 0) this catches the error raised by the function
        # this is not preferred to test exceptions

        with self.assertRaises(ValueError):
            calc.divide(10, 0)

if __name__ == '__main__':
    unittest.main()

'''
assertEqual(a, b)           a == b
assertNotEqual(a, b)        a != b

assertTrue(x)               bool(x) is True
assertFalse(x)              bool(x) is False

assertIs(a, b)              a is b
assertIsNot(a, b)           a is not b

assertIsNone(x)             x is None
assertIsNotNone(x)          x is not None

assertIn(a, b)              a in b
assertNotIn(a, b)           a not in b

assertIsInstance(a, b)      isinstance(a, b)
assertNotIsInstance(a, b)   not isinstance(a, b)

assertIsSubclass(a, b)      issubclass(a, b)
assertNotIsSubclass(a, b)   not issubclass(a, b)

'''