import unittest
from geometry.circle import circle
from geometry.rectangle import Rectangle 
from geometry.square import Square

#Class to check the test cases of class Circle in geometry module. 
class testcircle(unittest.TestCase):
    # Module to check initialization
    def test_initialization(self): 
        Circle=circle(5)
        self.assertEqual(Circle.radius,5)

    # Module to check the area of circle 
    def test_area(self):
        Circle=circle(5)
        self.assertAlmostEqual(Circle.area(),78.5,places=1)
    
    # Module to check the circumference of circle.
    def test_circumference(self):
        Circle = circle(5)
        self.assertAlmostEqual(Circle.circumference(),31.4,places=1)

    # Module to check the string representation. 
    def test_strep(self):
        Circle=circle(5)
<<<<<<< HEAD
        self.assertEqual(str(Circle),f'Circle radius: {5}, Area: {78.53981633974483}, Circumference: {31.41592653589793}')

=======
        self.assertTrue(Circle.__str__(),f'Circle radius: {5}, Area: {78.5}, Circumference: {31.4}')
    
    # Module to check the equality of two circle instances.
>>>>>>> 568f73a3d899a67f5e85486863236dac6fd8d3ca
    def test_eq(self):
        Circle1=circle(5)
        Circle2=circle(6)
        self.assertFalse(Circle1.area() == Circle2.area())

    # Module to check whether the area of the first circle instance is less than the other instance.
    def test_lessthan(self):
        Circle1=circle(5)
        Circle2=circle(6)
        self.assertTrue(Circle1.area()<Circle2.area())

# Module to check the test cases in class Rectangle in geometry module.
class testrectangle(unittest.TestCase):

    # Module to check the initialization of Rectangle object.    
    def test_initializer(self):
            rectangle = Rectangle(5,6)
            self.assertEqual(rectangle.width,5)
            self.assertEqual(rectangle.height,6)

    # Module to check the area of Rectangle    
    def test_area(self):
            rectangle=Rectangle(5,6)
            self.assertEqual(rectangle.area(),30)

    # Module to check the perimeter of Rectangle.
    def test_perimeter(self):
            rectangle=Rectangle(5,6)
            self.assertEqual(rectangle.perimeter(),22)

    # Module to check the string representation.
    def test_strep(self):
            rectangle=Rectangle(5,6)
            self.assertEqual(str(rectangle),f"Rectangle with width {5} and height {6}, Area: {30}, Perimeter: {22}")

    # Module to check the equality of area of rectangle with the area of other rectangle.
    def test_eq(self):
            rect1=Rectangle(5,5)
            rect2=Rectangle(6,6)
            self.assertFalse(rect1.area() == rect2.area())

    # Module to check whether the area of first rectangle class instance is less than the other instance.
    def test_lessthan(self):
            rect1=Rectangle(5,5)
            rect2=Rectangle(6,6)
            self.assertTrue(rect1.area()<rect2.area())

# Class to check the test cases of Class Square in geometry module.        
class testsquare(unittest.TestCase):

    # Module to check the initialization of an instance of class Square.
    def test_initialization(self):
        square=Square(5)
        self.assertEqual(square.side_length,5)

    # Module to check the area of Square.
    def test_area(self):
        square=Square(5)
        self.assertAlmostEqual(square.area(),25,places=1)
    
    # Module to check the perimeter of Square.
    def test_peri(self):
        square = Square(5)
        self.assertAlmostEqual(square.perimeter(),20)

    # Module to check the string representaion of an object of class Square.
    def test_strep(self):
        square=Square(5)
        self.assertEqual(str(square),f'Square with side length {5}, Area: {25}, Perimeter: {20}')

    # Module to check the equality of areas of two rectangle instances. 
    def test_eq(self):
        square1=Square(5)
        square2=Square(6)
        self.assertFalse(square1.area() == square2.area())

    # Module to check whether the area of one square is less than the area of other.
    def test_lessthan(self):
        square1=Square(5)
        square2=Square(6)
        self.assertTrue(square1.area()<square2.area())

if __name__ == '__main__':
    unittest.main()