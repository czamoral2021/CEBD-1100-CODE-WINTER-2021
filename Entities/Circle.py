from Entities.Shape import Shape
import math
# from Entities.Shape import Shape
# tonight
# Entities.Shape -> import the Shape.py file (path)
# import Shape -> the Class Shape


# This inherits from Shape, measurement is radius.


class Circle(Shape):

    def __init__(self, colour, material, radius):

        self.radius = radius
        # find a way to call the constructor of the parent "shape" here.

        super().__init__(colour, material)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius






    #
    # def get_info(self):
    #     print(self. radius + self.colour)

