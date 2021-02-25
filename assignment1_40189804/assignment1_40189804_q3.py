# [QUESTION 3] FIZZBUZZ
#
# Write a program that goes through a list of numbers, for this assignment – use a list of numbers from 0 to 25,
# including 25.
# • If the number is divisible by 3, print the number and "Fizz".
# • If the number is divisible by 5, print the number and "Buzz".
# • If the number is divisible by both, print the number and "FizzBuzz“
# • If the number is divisible by neither, print just the number.
# o Separate the number and "FizzBuzz" by a TAB character. (or use formatting to align everything).
# The goal, rather than just making it work, is to try to write it as clearly and efficiently as possible.
# This will be graded on efficient coding (not repeating things, no hard-coded constants, etc.)

# FizzBuzz Output
#
# 00:	FizzBuzz
# 01:
# 02:
# 03:	Fizz
# .
# 15:	FizzBuzz
# .
# 25:   Buzz
# .
# .

# This program will have a similar output, but until 150
# initialize variables and constant
MAX_NUMBER_RANGE = 151
y = ""
for x in range(MAX_NUMBER_RANGE):
    if x == MAX_NUMBER_RANGE:
        # break the For loop and ending the program
        break
    elif (int(x) % 3 == 0) and (int(x) % 5 != 0):
        # the number is divisible by 3 but not by 5, print the number and "Fizz"
        y = "\t Fizz"
        print("{0:3}: {1}".format(x, y))
        # {0:3} format allow to align the parameter #0 to the right until 3 digits
        # {1} it is the parameter #1
    elif (int(x) % 3 != 0) and (int(x) % 5 == 0):
        # the number is divisible by 5 but not by 3, print the number and "Buzz"
        y = "\t Buzz"
        print("{0:3}: {1}".format(x, y))
        # {0:3} format allow to align the parameter #0 to the right until 3 digits
        # {1} it is the parameter #1
    elif (int(x) % 5 == 0) and (int(x) % 3 == 0):
        # the number is divisible by 3 and 5, print the number and "FizzBuzz“
        y = "\t FizzBuzz"
        print("{0:3}: {1}".format(x, y))
        # {0:3} format allow to align the parameter #0 to the right until 3 digits
        # {1} it is the parameter #1
    else:
        if (int(x) % 5 != 0) and (int(x) % 3 != 0):
            # the number is not divisible by 3 and 5, print just the number
            y = "\t"
            print("{0:3}: {1}".format(x, y))
            # {0:3} format allow to align the parameter #0 to the right until 3 digits
            # {1} it is the parameter #1
# End program