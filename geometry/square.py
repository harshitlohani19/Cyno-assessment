class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        """
        Returns the area of the square.
        """
        return self.side_length**2

    def perimeter(self):
        """
        Returns the perimeter of the square.
        """
        return 4 * self.side_length

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return (
            f"Square with side length {self.side_length}, "
            f"Area: {self.area()}, Perimeter: {self.perimeter()}"
        )

    def __eq__(self, other):
        """
        Returns True if their areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __lt__(self, other):
        """
        Returns True if the area of the current square is less
        than the area of the other square, False otherwise.
        """
        return self.area() < other.area()
