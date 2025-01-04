import unittest
from _1_math import math

class TestMathFunctions(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(math.add(1, 1), 2)

if __name__ == '__main__':
    unittest.main()
