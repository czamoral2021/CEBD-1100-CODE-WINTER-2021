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

# initialize variables and constants
menu1 = ""
menu_triangle = ""
triangle_size = ""
# Isosceles triangle variables and constants
MAX_IS0_TRIANGLE = 15
v_triangle = 1
v_count = 1
v_string = ""
v_n_string = ""
v_iso = True
# Isosceles triangle variables and constants

while True:
    # Main Menu This leads to
    # # another menu (triangle menu)
    print("Main Menu")
    print("1 - Draw a Triangle")
    print("Q - Quit")
    menu1 = input("Enter a choice>")
    if menu1 == str(1):
        while True:
            # Triangle Menu
            print("Triangle Menu")
            print("1 – Right sided triangle")
            print("2 – Isosceles triangle")
            print("Q – Back Go back to the main")
            menu_triangle = input("Enter a choice>")
            if menu_triangle == str(1):
                print("Building a right sided triangle")
                triangle_size = input("Enter right sided triangle size > ")
                # validations
                if not triangle_size.isnumeric():
                    print("The right sided triangle size must be an integer number, try again.")
                    break
                else:
                    print("Right sided triangle in process.")
            if menu_triangle == str(2):
                while v_iso:
                    print("Building an Isosceles triangle")
                    triangle_size = input("Enter Isosceles triangle size > ")
                    # validations
                    # if triangle_size == 'q' or "Q":
                    #     v_iso = False
                    if not triangle_size.isnumeric() or triangle_size.isnumeric() == "0":
                        print("The Isosceles triangle size must be an integer number greater than zero, try again.")
                        continue
                    elif int(triangle_size) % 2 == 0:
                        print("The Isosceles triangle size must be an ODD integer number, try again.")
                        continue
                    elif MAX_IS0_TRIANGLE < int(triangle_size) > 0:
                        print(f"Triangle size issues, please between 1 and {MAX_IS0_TRIANGLE} maximum allowed")
                        continue
                    elif v_iso:
                        print("Isosceles triangle in process.")
                        # v_triangle even => please enter an ODD base triangle and greater than 1
                        v_triangle = int(triangle_size)
                        for y in range(1, int(v_triangle) + 1):
                            if v_count % 2 != 0:
                                v_string = v_count * "*"
                                v_n_string = str.center(v_string, v_triangle, ' ')
                                print(v_n_string)
                            v_count += 1
                        v_triangle = 1
                        v_count = 1
                        v_string = ""
                        v_n_string = ""
                        break
            if menu_triangle == "Q" or menu_triangle == "q":
                print("Go to previous menu")
                break
    if menu1 == "Q" or menu1 == "q":
        print("Exiting program")
        break

