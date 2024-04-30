import math


class Circle:
    def __init__(self, radius):
        """
        Constructor to initialize the radius.
        """
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle.
        """
        area = math.pi * self.radius**2
        return area

    def circumference(self):
        """
        Calculates and return the circumference of the circle.
        """
        circumference = 2 * math.pi * self.radius
        return circumference

    def __str__(self):
        """
        Returns a string representation of the Circle object.
        """
        str_repr = f"Circle radius: {self.radius}"
        return str_repr

    def __eq__(self, other):
        """
        Checks if the areas of two circles are equal.
        """
        aeq = self.area() == other.area()
        return aeq

    def __lt__(self, other):
        """
        Checks if the area of the current
        circle is less than the area of another circle.
        """
        lt = self.area() < other.area()
        return lt
