import math


class Circle:
    def __init__(self, radius) -> None:
        """
        Constructor to initialize the radius.
        """
        self.radius = radius

    def area(self) -> float:
        """
        Returns the area of the circle.
        """
        area = math.pi * self.radius**2
        return area

    def circumference(self) -> float:
        """
        Returns the circumference of the circle.
        """
        circumference = 2 * math.pi * self.radius
        return circumference

    def __str__(self) -> str:
        """
        Returns a string representation of the Circle object.
        """
        str_repr = f"Circle radius: {self.radius}"
        return str_repr

    def __eq__(self, other) -> bool:
        """
        Checks if the areas of two circles are equal.
        """
        aeq = self.radius == other.radius
        return aeq

    def __lt__(self, other) -> bool:
        """
        Checks if the area of the current
        circle is less than the area of another circle.
        """
        lt = self.radius < other.radius
        return lt
