import math


class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius

    @property
    def area(self) -> float:
        """
        Calculates the area of the circle.
        @params:
        @return: float
        """
        area = math.pi * self.radius**2
        return area

    @property
    def circumference(self) -> float:
        """
        Calculates the circumference of the circle.
        @params:
        @return: float
        """
        circumference = 2 * math.pi * self.radius
        return circumference

    def __str__(self) -> str:
        """
        Returns a string representation of the Circle object.
        @params:
        @returns: str
        """
        str_repr = f"Circle radius: {self.radius}"
        return str_repr

    def __eq__(self, other) -> bool:
        """
        Checks if the areas of two circles are equal.
        @params:
        @returns:bool
        """
        aeq = self.radius == other.radius
        return aeq

    def __lt__(self, other) -> bool:
        """
        Checks if the area of the current
        circle is less than the area of another circle.
        @params:
        @returns:bool
        """
        lt = self.radius < other.radius
        return lt
