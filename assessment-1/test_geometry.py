import unittest
from geometry.circle import circle
from geometry.rectangle import Rectangle 
from geometry.square import Square

class testcircle(unittest.TestCase):
    def test_initialization(self):
        Circle=circle(5)
        self.assertEqual(Circle.radius,5)

    def test_area(self):
        Circle=circle(5)
        self.assertAlmostEqual(Circle.area(),78.5,places=1)
    
    def test_circumference(self):
        Circle = circle(5)
        self.assertAlmostEqual(Circle.circumference(),31.4,places=1)

    def test_strep(self):
        Circle=circle(5)
        self.assertTrue(Circle.__str__(),f'Circle radius: {5}, Area: {78.5}, Circumference: {31.4}')

    def test_eq(self):
        Circle1=circle(5)
        Circle2=circle(6)
        self.assertFalse(Circle1.area() == Circle2.area())

    def test_largerthan(self):
        Circle1=circle(5)
        Circle2=circle(6)
        self.assertTrue(Circle1.area()<Circle2.area())

class testrectangle(unittest.TestCase):
        def test_initializer(self):
            rectangle = Rectangle(5,6)
            self.assertEqual(rectangle.width,5)
            self.assertEqual(rectangle.height,6)
        


if __name__ == '__main__':
    unittest.main()