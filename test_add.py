import unittest
import calc

class TestAdd(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(calc.add(1,2), 4)
        self.assertEqual(calc.add(10,100), 110)
        self.assertEqual(calc.add(5,5), 10)
        self.assertEqual(calc.add(20,200), 220)

    def testMult(self):
        self.assertEqual(calc.mult(1,2), 2)
        self.assertEqual(calc.mult(10,10), 100)

if __name__ == "__main__":
    unittest.main()
