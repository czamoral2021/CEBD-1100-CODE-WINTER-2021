# Exercise 3
# (5 minutes)
# Create a function that adds two numbers and returns the value.
# Use your function in your code, in some scenario.

def add_two_nums(val1, val2):
    return val1 + val2


num1 = float(input("Enter the first number to add > "))
num2 = float(input("Enter the second number to add > "))
if add_two_nums(num1, num2):
    print("The addition between {} and {} is > ".format(num1, num2), end="")
    print(add_two_nums(num1, num2))

