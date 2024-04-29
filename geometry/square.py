class Square:
    """
    Square class to represent a square and its properties.
    """

    def __init__(self, side_length):
        """
        Method to initialize an object of Square class with the provided
        side length.
        """
        self.side_length = side_length

    def area(self):
        """
        Method to calculate and return the area of the square.
        """
        return self.side_length**2

    def perimeter(self):
        """
        Method to calculate and return the perimeter of the square.
        """
        return 4 * self.side_length

    def __str__(self):
        """
        Method to return the string representation of the square, including
        its side length, area, and perimeter.
        """
        return (
            f"Square with side length {self.side_length}, "
            f"Area: {self.area()}, Perimeter: {self.perimeter()}"
        )

    def __eq__(self, other):
        """
        Method to compare the area of the current square with another
        square. Returns True if their areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __lt__(self, other):
        """
        Method to compare the area of the current square with another
        square. Returns True if the area of the current square is less
        than the area of the other square, False otherwise.
        """
        return self.area() < other.area()
