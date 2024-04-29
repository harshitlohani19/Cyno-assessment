class Rectangle:
    """
    Method to initialize an object of class Rectangle with given values of
    width and height.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    """
    Method to return the area of the rectangle.
    """

    def area(self):
        return self.width * self.height

    """
    Method to return the perimeter of the rectangle.
    """

    def perimeter(self):
        return 2 * (self.width + self.height)

    """
    Method to return a string representation of the rectangle including its 
    width, height, area and perimeter.
    """

    def __str__(self):
        return (
            f"Rectangle with width {self.width} and height {self.height}, "
            f"Area: {self.area()}, Perimeter: {self.perimeter()}"
        )

    """
    Method to compare the area of current rectangle with another rectangle,
    return True if equal, False otherwise.
    """

    def __eq__(self, other):
        return self.area() == other.area()

    """
    Method to compare area of current rectangle with another rectangle and
    return True if area of the current rectangle is less than the area of the
    other rectangle, False otherwise.
    """

    def __lt__(self, other):
        return self.area() < other.area()
