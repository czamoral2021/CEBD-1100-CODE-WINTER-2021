class TwoValueCalculator:

    def __init__(self):

        self.v1 = 0
        self.v2 = 0

    def add(self):
        return self.v1 + self.v2

    def substract(self):
        return self.v1 - self.v2

    def modulus(self):
        return self.v1 % self.v2



my_calculator = TwoValueCalculator()


print(my_calculator.add())


print(my_calculator.add())

