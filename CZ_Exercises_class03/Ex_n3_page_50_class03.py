# Exercise - 3
# Modify exercise 2 to prompt the user to provide a number, then determine
# that the number is even or odd.
# The program needs to ask the user if he want to continue or not, if yes, then
# the program asks for another number, if No, then the programs ends.

# initialize variables

answer = ""

while answer != "s":
    answer = input("Enter a positive integer number (enter \"S or s\" to stop)>")
    if answer[0:1].upper() == "S":
        break
    elif answer.isnumeric():
        if int(answer) % 2 == 0:
            print(answer + " is an even number")
        else:
            print(answer + " is an odd number")
    if not answer.isnumeric():
        print(answer + " is not a positive integer number")

