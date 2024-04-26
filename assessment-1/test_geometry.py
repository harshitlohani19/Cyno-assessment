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
        
        def test_area(self):
            rectangle=Rectangle(5,6)
            self.assertEqual(rectangle.area(),30)

        def test_perimeter(self):
            rectangle=Rectangle(5,6)
            self.assertEqual(rectangle.perimeter(),22)

        def test_strep(self):
            rectangle=Rectangle(5,6)
            self.assertTrue(rectangle.__str__(),f"Rectangle with width {5} and height {6}, Area: {30}, Perimeter: {22}")

        def test_eq(self):
            rect1=Rectangle(5,5)
            rect2=Rectangle(6,6)
            self.assertFalse(rect1.area() == rect2.area())

        def test_largerthan(self):
            rect1=Rectangle(5,5)
            rect2=Rectangle(6,6)
            self.assertTrue(rect1.area()<rect2.area())
        
class testsquare(unittest.TestCase):
    def test_initialization(self):
        square=Square(5)
        self.assertEqual(square.side_length,5)

    def test_area(self):
        square=Square(5)
        self.assertAlmostEqual(square.area(),25,places=1)
    
    def test_peri(self):
        square = Square(5)
        self.assertAlmostEqual(square.perimeter(),20)

    def test_strep(self):
        square=Square(5)
        self.assertTrue(square.__str__(),f'Square with side length {5}, Area: {25}, Perimeter: {20}')

    def test_eq(self):
        square1=Square(5)
        square2=Square(6)
        self.assertFalse(square1.area() == square2.area())

    def test_largerthan(self):
        square1=Square(5)
        square2=Square(6)
        self.assertTrue(square1.area()<square2.area())
        
if __name__ == '__main__':
    unittest.main()