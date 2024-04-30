import unittest
from geometry.circle import Circle
from geometry.rectangle import Rectangle
from geometry.square import Square


class TestCircle(unittest.TestCase):

    def test_initialization(self):
        circle = Circle(5)
        self.assertEqual(circle.radius, 5)

    def test_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.5, places=1)

    def test_circumference(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.circumference(), 31.4, places=1)

    def test_strep(self):
        circle = Circle(5)
        self.assertEqual(str(circle), f"Circle radius: {5}")

    def test_eq(self):
        circle1 = Circle(5)
        circle2 = Circle(6)
        self.assertFalse(circle1.area() == circle2.area())

    def test_lessthan(self):
        circle1 = Circle(5)
        circle2 = Circle(6)
        self.assertTrue(circle1.area() < circle2.area())


class Testrectangle(unittest.TestCase):

    def test_initializer(self):
        rectangle = Rectangle(5, 6)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 6)

    def test_area(self):
        rectangle = Rectangle(5, 6)
        self.assertEqual(rectangle.area(), 30)

    def test_perimeter(self):
        rectangle = Rectangle(5, 6)
        self.assertEqual(rectangle.perimeter(), 22)

    def test_str(self):
        rectangle = Rectangle(5, 6)
        expected_output = f"Rectangle with width {5} and height {6}"
        self.assertEqual(str(rectangle), expected_output)

    def test_eq(self):
        rect1 = Rectangle(5, 5)
        rect2 = Rectangle(6, 6)
        self.assertFalse(rect1.area() == rect2.area())

    def test_lessthan(self):
        rect1 = Rectangle(5, 5)
        rect2 = Rectangle(6, 6)
        self.assertTrue(rect1.area() < rect2.area())


class Testsquare(unittest.TestCase):
    def test_initialization(self):
        square = Square(5)
        self.assertEqual(square.side_length, 5)

    def test_area(self):
        square = Square(5)
        self.assertAlmostEqual(square.area(), 25, places=1)

    def test_peri(self):
        square = Square(5)
        self.assertAlmostEqual(square.perimeter(), 20)

    def test_str(self):
        square = Square(5)
        expected_output = (
            f"Square with side length {5}, " f"Area: {25}, Perimeter: {20}"
        )
        self.assertEqual(str(square), expected_output)

    def test_eq(self):
        square1 = Square(5)
        square2 = Square(6)
        self.assertFalse(square1.area() == square2.area())

    def test_lessthan(self):
        square1 = Square(5)
        square2 = Square(6)
        self.assertTrue(square1.area() < square2.area())


if __name__ == "__main__":
    unittest.main()
