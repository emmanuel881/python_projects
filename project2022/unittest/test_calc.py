import unittest
import calc

class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)

if __name__ == "__main__":
    unittest.main()
