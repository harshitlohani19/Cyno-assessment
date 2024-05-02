class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    @property
    def area(self) -> float:
        """
        Calculates the area of the square.
        @params:
        @return: float

        """
        return self.side_length**2

    @property
    def perimeter(self) -> float:
        """
        Calculates the perimeter of the square.
        @params:
        @return: float
        """
        return 4 * self.side_length

    def __str__(self) -> str:
        """
        Returns the string representation of the square.
        @params:
        @return: str
        """
        return f"Square with side length {self.side_length}"

    def __eq__(self, other) -> bool:
        """
        Returns True if their areas are equal, False otherwise.
        @params:
        @return: bool
        """
        return self.side_length == other.side_length

    def __lt__(self, other) -> bool:
        """
        Returns True if the area of the current square is less
        than the area of the other square, False otherwise.
        @params:
        @return: bool
        """
        return self.side_length < other.side_length
