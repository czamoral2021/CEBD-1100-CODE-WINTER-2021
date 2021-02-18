# At home draw a triangle
# ask the user how big the triangle should be, then draw the triangle.
# Use *2* methods to do this. (1) Using nested loops, (2) using the multiplication symbol.
# Use the "#" character to draw the triangle.

# Method 2

# for x in range(0, size):
#     print("#" * size)

# initialize variables

v_triangle = ""

while v_triangle != "s":
    v_triangle = input("Enter triangle size as integer number (enter \"S or s\" to stop)>")
    v_count = 0
    if v_triangle[0:1].upper() == "S":
        break
    elif not v_triangle.isnumeric():
        print("triangle size is not an integer number")
    else:
        v_count = int(v_triangle)
        if 2 <= int(v_triangle) < 10:
            for y in range(1, int(v_triangle) + 1):
                print("# " * v_count)
                # v_count = v_count - 1
                v_count -= 1
        else:
            print("Triangle size issues, please between 2 and 9")




# Method 1

# for y in range(0, size):
#     for x in range (0, size):
#         print("%", end="")
#     print()

# initialize variables

# v_triangle = ""
#
# while v_triangle != "s":
#     v_triangle = input("Enter triangle size as integer number (enter \"S or s\" to stop)>")
#     v_count = 0
#     if v_triangle[0:1].upper() == "S":
#         break
#     elif not v_triangle.isnumeric():
#         print("triangle size is not an integer number")
#     else:
#         v_count = int(v_triangle)
#         if int(v_triangle) >= 2 and int(v_triangle) < 10:
#             for y in range(1, int(v_triangle) + 1):
#                 for x in range(1, int(v_triangle) + 1):
#                     print("# " * v_count)
#                     v_count -= 1
#             print()    ### print empty
#         else:
#             print("Triangle size issues, please between 2 and 9")


