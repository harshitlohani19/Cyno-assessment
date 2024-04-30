import unittest
from geometry.circle import circle
from geometry.rectangle import Rectangle
from geometry.square import Square


class TestCircle(unittest.TestCase):

    def test_initialization(self):
        Circle = circle(5)
        self.assertEqual(Circle.radius, 5)

    def test_area(self):
        """checks the area of circle"""
        Circle = circle(5)
        self.assertAlmostEqual(Circle.area(), 78.5, places=1)

    def test_circumference(self):
        """checks the circumference of circle."""
        Circle = circle(5)
        self.assertAlmostEqual(Circle.circumference(), 31.4, places=1)

    def test_strep(self):
        """checks the string representation."""
        Circle = circle(5)
        self.assertEqual(str(Circle), f"Circle radius: {5}")

    def test_eq(self):
        """checks the equality of 2 Circles"""
        Circle1 = circle(5)
        Circle2 = circle(6)
        self.assertFalse(Circle1.area() == Circle2.area())

    def test_lessthan(self):
        """checks whether the area of the first circle instance is
        less than the other instance."""
        Circle1 = circle(5)
        Circle2 = circle(6)
        self.assertTrue(Circle1.area() < Circle2.area())


class testrectangle(unittest.TestCase):

    def test_initializer(self):
        rectangle = Rectangle(5, 6)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)

    def test_area(self):
        """checks the area of Rectangle"""
        rectangle = Rectangle(5, 6)
        self.assertEqual(rectangle.area(), 30)

    def test_perimeter(self):
        """checks the perimeter of Rectangle."""
        rectangle = Rectangle(5, 6)
        self.assertEqual(rectangle.perimeter(), 22)

    def test_str(self):
        """checks the string representation."""
        rectangle = Rectangle(5, 6)
        rectangle
        expected_output = f"Rectangle with width {5} and height {6}"
        self.assertEqual(str(rectangle), expected_output)

    def test_eq(self):
        """checks the equality of area of rectangle with the area of
        other rectangle."""
        rect1 = Rectangle(5, 5)
        rect2 = Rectangle(6, 6)
        self.assertFalse(rect1.area() == rect2.area())

    def test_lessthan(self):
        """checks whether the area of first rectangle class instance
        is less than the other instance."""
        rect1 = Rectangle(5, 5)
        rect2 = Rectangle(6, 6)
        self.assertTrue(rect1.area() < rect2.area())


class testsquare(unittest.TestCase):
    def test_initialization(self):
        square = Square(5)
        self.assertEqual(square.side_length, 5)

    def test_area(self):
        """checks the area of Square."""
        square = Square(5)
        self.assertAlmostEqual(square.area(), 25, places=1)

    def test_peri(self):
        """checks the perimeter of Square."""
        square = Square(5)
        self.assertAlmostEqual(square.perimeter(), 20)

    def test_str(self):
        """checks the string representaion of an object of class Square."""
        square = Square(5)
        expected_output = (
            f"Square with side length {5}, " f"Area: {25}, Perimeter: {20}"
        )
        self.assertEqual(str(square), expected_output)

    def test_eq(self):
        """checks the equality of areas of two rectangle instances."""
        square1 = Square(5)
        square2 = Square(6)
        self.assertFalse(square1.area() == square2.area())

    def test_lessthan(self):
        """checks whether the area of one square is less than
        the area of other."""
        square1 = Square(5)
        square2 = Square(6)
        self.assertTrue(square1.area() < square2.area())


if __name__ == "__main__":
    unittest.main()
