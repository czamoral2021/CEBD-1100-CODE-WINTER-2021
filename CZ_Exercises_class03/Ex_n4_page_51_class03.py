# print 10 random values of numbers between 1 and 100.
# The random.randint function takes two arguments: the start and the end of the range for the generated integer values.

# import random
# for x in range(10):
#     print(random.randint(0,101))
###################################################################################################################
# Exercise - 4: Guessing Numbers
# Write a program that choose an integer between 0 and 100, inclusive. The
# program prompts the user to enter a number continuously until the number
# matches the chosen number. For each user input, the program tells the user
# whether the input is too low or too high, so the user can choose the next
# input intelligently.
# After the user guess correctly, the program will print: “Bravo you guess
# correctly after ... times

# initialize variables
import random
answer = ""
v_low = 0
v_high = 0
v_random = 0
v_cont = 0

while answer != "s":
    answer = input("Enter a positive integer number (enter \"S or s\" to stop)>")
    if answer[0:1].upper() == "S":
        break
    elif answer.isnumeric():
        v_random = random.randint(0, 101)
        v_cont += 1
        print("the random number is :" + str(v_random))
        print("your choice is :" + answer)
        if int(answer) == v_random:
            print("Bravo you guess correctly after " + str(v_cont) + "... times")
            print("your choice number just matched: " + str(random) + " machine" + answer + " choice")
        else:
            if (v_random - int(answer)) > 0 and (v_random - int(answer)) > 20:
                print("the input is too low")
            else:
                if (v_random - int(answer)) < 0 and (int(answer) - v_random) > 20:
                    print("the input is too high")
                else:
                    print("you are closer by chance")
    if not answer.isnumeric():
        print(answer + " is not a positive integer number")