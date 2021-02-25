def add_numbers(n1, n2, n3=0, n4=0):
    return n1 + n2 + n3 + n4


def add_numbers2(numbers: list):
    return sum(numbers)


print("Sum of numbers " + str(add_numbers2([5, 8, 3, 6, 8, 4])))
