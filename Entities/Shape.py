import datetime

class Shape:

    def __init__(self, colour, material):
        self.colour = colour
        self.material = material
        self.create_date = datetime.datetime.now().strftime("%x")

        # this date will be the same for all Shapes, we do not need to pass this create parameter

