def is_divisible_by(num, divisor):
    # Avoid a /div0 error
    if divisor == 0:
        return False
    return num % divisor == 0


num = float(input("Enter a number > "))
divisor = float(input("Enter a number to see if divisible > "))
if is_divisible_by(num, divisor):
    print("The number {} is divisible by {}".format(num, divisor))
else:
    print("Not divisible by divisor (or zero was supplied)")