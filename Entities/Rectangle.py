from Entities.Square import Square

class Rectangle(Square):

    def __init__(self, colour, material, bottom_side, right_side):

        self.right_side = right_side
        # find a way to call the constructor of the parent "shape" here.

        super().__init__(colour, material, bottom_side)
        # from Square and from Square

    def area(self):
        return self.bottom_side * self.right_side

    def perimeter(self):
        return (self.bottom_side + self.right_side) * 2






    #
    # def get_info(self):
    #     print(self. radius + self.colour)

