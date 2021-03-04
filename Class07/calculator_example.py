class TwoValueCalculator:

    def __init__(self, value1, value2):

        self.v1 = value1
        self.v2 = value2

    def add(self):
        return self.v1 + self.v2

    def substract(self):
        return self.v1 - self.v2

    def modulus(self):
        return self.v1 % self.v2

my_calculator = TwoValueCalculator(5,6)

print(my_calculator.add())

my_calculator.v1 = 1
my_calculator.v2 = 2

print(my_calculator.add())

