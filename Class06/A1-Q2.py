while True:
    # Main Menu
    print("A: student menu")
    print("B: instructor menu")
    print("Q: Quit")
    menu1 = input("Enter a choice>")

    if menu1 == "A":
        while True:

            # Student Menu
            print("Student Menu")
            print("A: View grades")
            print("B: Pay tuition")
            print("Q: Quit")
            menu_student = input("Enter a choice>")
            if menu_student == "B":
                tuition_amount = input("Enter amount to be paid today.")
                if not tuition_amount.isnumeric():
                    print("The amount must be a number, try again.")
                else:
                    print("do something with amount entered.")

            if menu_student == "Q":
                print("Go to previous menu")
                break
    if menu1 == "Q":
        print("Exiting program")
        break