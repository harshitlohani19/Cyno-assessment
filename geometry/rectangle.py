class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    @property
    def area(self) -> float:
        """
        Returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        """
        Returns a string representation of the rectangle.
        """
        return f"Rectangle with width {self.width} and height {self.height}"

    def __eq__(self, other) -> bool:
        """
        Returns True if equal, False otherwise.
        """
        return self.area == other.area

    def __lt__(self, other) -> bool:
        """
        Returns True if area of the current rectangle is less than the area
        of the other rectangle, False otherwise.
        """
        return self.area < other.area
