def add_numbers(val1, val2):
    return val1 + val2


num1 = float(input("Enter the first number >"))
num2 = float(input("Enter the second number >"))

print("The sum of both numbers is " + str(add_numbers(num1, num2)))


print(add_numbers(9, 5))

print(add_numbers("9", "5"))
