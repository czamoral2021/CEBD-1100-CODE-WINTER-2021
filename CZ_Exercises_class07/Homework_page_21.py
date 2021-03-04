# Homework
# Make a function that will print out a row of asterisks depending on the value
# given to it.
#  Use this in a loop – so we can print a triangle of stars.

# Output:
#
# *
# **
# ***

# Example with a fix size assigned

# def func_triangle(v_triangle: int):
#     for y in range(1, int(v_triangle) + 1):
#         print("* " * y)
#     return print("this is the triangle")
#
# l1 = 5
# func_triangle(l1)
# print()

def func_triangle(v_triangle: str = ""):
    for y in range(1, int(v_triangle) + 1):
        print("* " * y)
    return print("This is the triangle")


v_size = ""
while v_size != "s":
    v_size = input("Enter triangle size as integer number (enter \"S or s\" to stop)>")
    # v_count = 0
    if v_size[0:1].upper() == "S":
        break
    elif not v_size.isnumeric():
        print("triangle size is not an integer number")
    else:
        if 2 <= int(v_size) < 10:
            func_triangle(v_size)
        else:
            print("Triangle size issues, please between 2 and 9")