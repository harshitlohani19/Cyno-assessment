class Square:
    def __init__(self, side_length) -> None:
        self.side_length = side_length

    @property
    def area(self) -> float:
        """
        Returns the area of the square.
        """
        return self.side_length**2

    @property
    def perimeter(self) -> float:
        """
        Returns the perimeter of the square.
        """
        return 4 * self.side_length

    def __str__(self) -> str:
        """
        Returns the string representation of the square.
        """
        return f"Square with side length {self.side_length}"

    def __eq__(self, other) -> bool:
        """
        Returns True if their areas are equal, False otherwise.
        """
        return self.side_length == other.side_length

    def __lt__(self, other) -> bool:
        """
        Returns True if the area of the current square is less
        than the area of the other square, False otherwise.
        """
        return self.side_length < other.side_length
