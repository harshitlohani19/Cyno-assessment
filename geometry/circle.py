import math


class circle:
    """
    Circle class to calculate area and circumference of a circle.
    """

    def __init__(self, radius):
        """
        Constructor to initialize the radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Method to calculate and return the area of the circle.
        """
        area = math.pi * self.radius**2
        return area

    def circumference(self):
        """
        Method to calculate and return the circumference of the circle.
        """
        circumference = 2 * math.pi * self.radius
        return circumference

    def __str__(self):
        """
        Method to return a string representation of the Circle object.
        """
        str_repr = (
            f"Circle radius: {self.radius}"
        )
        return str_repr

    def __eq__(self, other):
        """
        Method to check if the areas of two circles are equal.
        """
        aeq = self.area() == other.area()
        return aeq

    def __lt__(self, other):
        """
        Method to check if the area of the current
        circle is less than the area of another circle.
        """
        lt = self.area() < other.area()
        return lt
