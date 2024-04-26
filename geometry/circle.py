import math


class circle:
    '''
    Circle class to calculate area and circumference of a circle
    '''

    def __init__(self, radius):
        '''
        Constructor to initialize the radius of the circle
        '''

        self.radius = radius

    # Method to return Circle Area
    def area(self):
        area = math.pi * self.radius**2
        return area

    # Method to return Cicle Circumference
    def circumference(self):
        circumference = 2*math.pi*self.radius
        return circumference

    # Method to return string representation
    def __str__(self):
        str = f"Circle radius: {self.radius}, Area: {self.area()}, Circumference: {self.circumference()}"
        return str

    # Method to check if areas are equal or not,returns True/False
    def __eq__(self, other):
        aeq = self.area() == other.area()
        return aeq

    # Method to Check if area1 is < than area2,returns True/False
    def __lt__(self, other):
        lt = self.area() < other.area()
        return lt
