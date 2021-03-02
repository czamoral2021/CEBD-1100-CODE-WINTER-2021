# Exercise 2
# (5 minutes)
#  Write a function that gets a number as its parameter and then returns True if
# the number is divisible by 3 otherwise it will return False.
#  Use your function to prompt a number from the user and print if the number
# is divisible by 3 or not.
#  Pro Tip: As a developer, you want to make your function as flexible as
# possible. Try to find a way NOT to hard code the number “3” in the function.
# provide a number: 15
# 15 is divisible by 3


def is_divisible_by_3(a, b):
    if b == 0:
        return False
    return a % b == 0


v_num = float(input("Enter a number > "))
v_divisor = 2
if is_divisible_by_3(v_num, v_divisor):
    print("The number {} is divisible by {}".format(v_num, v_divisor))
elif v_divisor == 0:
    print(f"{v_divisor} is invalid divisor")
else:
    print(f"Not divisible by {v_divisor}")