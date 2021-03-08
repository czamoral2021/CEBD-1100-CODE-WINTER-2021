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

my_calculator.v1 = 10
my_calculator.v2 = 11

print(my_calculator.add())

my_calculator.v1 = 1
my_calculator.v2 = 2

print(my_calculator.add())

