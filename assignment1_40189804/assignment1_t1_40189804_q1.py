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
                tuition_amount = input("Enter right sided triangle size > ")
                # validations
                if not tuition_amount.isnumeric():
                    print("The right sided triangle size must be an integer number, try again.")
                    break
                else:
                    print("do the right sided triangle.")
            if menu_triangle == str(2):
                print("Building a Isosceles triangle")
                tuition_amount = input("Enter Isosceles triangle size > ")
                # validations
                if not tuition_amount.isnumeric():
                    print("The Isosceles triangle size must be an integer number, try again.")
                    break
                else:
                    print("do the Isosceles triangle.")
            if menu_triangle == "Q" or menu_triangle == "q":
                print("Go to previous menu")
                break
            else:
                print("Invalid choice in Triangle Menu")
    if menu1 == "Q" or menu1 == "q":
        print("Exiting program")
        break
    else:
        print("Invalid choice in Main Menu")