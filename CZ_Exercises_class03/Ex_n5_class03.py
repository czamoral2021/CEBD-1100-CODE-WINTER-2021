# c.Ex_n5_class03

# Multiples of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

# initialize variables

answer = ""

while answer != "q":
    answer = input("Enter a positive integer number (enter \"Q or q\" to stop)>")
    if answer[0:1].upper() == "Q":
        break
    elif answer.isnumeric():
        if int(answer) % 10 == 0:
            print(answer + " is a multiple of ten.")
        else:
            print(answer + " is not a multiple of ten.")
    if not answer.isnumeric():
        print(answer + " is not a positive integer number")

