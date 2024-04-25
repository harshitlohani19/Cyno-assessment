import unittest
from geometry.circle import circle 

class testcircle(unittest.TestCase):
    def test_initialization(self):
        Circle=circle(5)
        self.assertEqual(Circle.radius,5)

    def test_area(self):
        Circle=circle(5)
        self.assert

if __name__ == '__main__':
    unittest.main()