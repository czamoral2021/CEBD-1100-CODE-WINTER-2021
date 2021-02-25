# [QUESTION 1] SHAPES
#
# Create a menu system allowing the user to draw shapes, with the ability to quit the program when needed.
# The menu should look like this (Don’t include the parts in blue). The triangle menus should ask the user what SIZE
# the shape should be.
#
# Main Menu
# 1 - Draw a Triangle This leads to
# another menu (triangle menu)
# Q - Quit
#
# Triangle Menu
# 1 – Right sided triangle
# 2 – Isosceles triangle
# Q – Back Go back to the main
# menu
#
# Errors should be prevented when possible – such as entering a menu choice that doesn't exist, entering a letter
# instead of a number (for size), and importantly for a isosceles triangle you must enter a number that’s ODD and
# greater than 0. Eg: You cannot draw a perfect isosceles triangle with a size of 4.

# This program has limits for each kind of triangle.
# Isosceles triangle (15). Right sided triangle (14)

# initialize variables and constants
menu1 = ""
menu_triangle = ""
triangle_size = ""
# Isosceles triangle variables and constants
MAX_IS0_TRIANGLE = 15
v_iso = True
# Right sided triangle variables and constants
MAX_RS_TRIANGLE = 14
v_rst = True
#

while True:
    # Main Menu This leads to
    # # another menu (triangle menu)
    print("Main Menu")
    print("1 - Draw a Triangle")
    print("Q - Quit")
    menu1 = input("Enter a valid choice, invalid --> Main Menu > ")
    if menu1 == str(1):
        while True:
            # Triangle Menu
            print("Triangle Menu")
            print("1 – Right sided triangle")
            print("2 – Isosceles triangle")
            print("Q – Go back to the main menu")
            menu_triangle = input("Enter a valid choice, invalid --> Triangle Menu > ")
            if menu_triangle == str(1):
                while v_rst:
                    v_triangle = 1
                    v_count = 1
                    print("Building a Right sided triangle")
                    triangle_size = input("Enter Right sided triangle size(integer), 1 --> Triangle Menu > ")
                    # validations
                    if not triangle_size.isnumeric():
                        print("The Right sided triangle size must be an integer number greater than one, try again.")
                        continue
                    elif MAX_RS_TRIANGLE < int(triangle_size) or int(triangle_size) == 0:
                        print(f"Right sided triangle size issues, please between 1 and {MAX_RS_TRIANGLE} maximum allowed")
                        continue
                    elif v_rst and int(triangle_size) > 1:
                        print("Right sided triangle below.")
                        v_triangle = int(triangle_size)
                        for y in range(1, int(v_triangle) + 1):
                            print("* " * v_count)
                            v_count += 1
                        print()
                        break
                    else:
                        break
            if menu_triangle == str(2):
                while v_iso:
                    v_triangle = 1
                    v_count = 1
                    v_string = ""
                    v_n_string = ""
                    print("Building an Isosceles triangle")
                    triangle_size = input("Enter Isosceles triangle size(integer), 1 --> Triangle Menu > ")
                    # validations
                    if not triangle_size.isnumeric():
                        print("The Isosceles triangle size must be an integer number greater than one, try again.")
                        continue
                    elif int(triangle_size) % 2 == 0:
                        print("The Isosceles triangle size must be an ODD integer number, try again.")
                        continue
                    elif MAX_IS0_TRIANGLE < int(triangle_size) or int(triangle_size) == 0:
                        print(f"Isosceles triangle issues, please between 1 and {MAX_IS0_TRIANGLE} maximum allowed")
                        continue
                    elif v_iso and int(triangle_size) > 1:
                        print("Isosceles triangle below.")
                        v_triangle = int(triangle_size)
                        for y in range(1, int(v_triangle) + 1):
                            if v_count % 2 != 0:
                                v_string = v_count * "*"
                                v_n_string = str.center(v_string, v_triangle, ' ')
                                print(v_n_string)
                            v_count += 1
                        print()
                        break
                    else:
                        break
            if menu_triangle == "Q" or menu_triangle == "q":
                print("Go to previous menu")
                break
    if menu1 == "Q" or menu1 == "q":
        print("Exiting program")
        break

