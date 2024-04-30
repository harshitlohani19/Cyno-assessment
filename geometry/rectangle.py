class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Method to return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle including its
        width, height, area and perimeter.
        """
        return f"Rectangle with width {self.width} and height {self.height}"

    def __eq__(self, other):
        """
        Compares the area of current rectangle with another rectangle,
        return True if equal, False otherwise.
        """
        return self.area() == other.area()

    def __lt__(self, other):
        """
        Compares area of current rectangle with another rectangle and
        return True if area of the current rectangle is less than the area
        of the other rectangle, False otherwise.
        """
        return self.area() < other.area()
