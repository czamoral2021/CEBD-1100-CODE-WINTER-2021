def generate_salutation(first: str, last: str = "Unknown"):
    return first + last


def generate_salutation2(first="", last: str = "Unknown"):
    return first + last


print(generate_salutation("Brendan", "Wood"))


def add_two_numbers(num1=0, num2=0):
    return num1 + num2

# num2 = add_two_numbers(6, "Jack")
# # it will crash because the type is defined numeric




