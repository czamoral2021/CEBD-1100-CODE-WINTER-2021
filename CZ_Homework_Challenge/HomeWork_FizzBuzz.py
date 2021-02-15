# Homework Challenge: FizzBuzz
# Print a list of numbers from 0 to 25, including 25.
# If the number is divisible by 3, print the number and "Fizz".
# If the number is divisible by 5, print the number and "Buzz".
# If the number is divisible by both, print the number and "FizzBuzz“
# If the number is divisible by neither, print just the number.
# Separate the number and "FizzBuzz" by a TAB character.
# Note, this is a commonly asked question at job interviews.
# The goal, rather than just making it work, is to try to write it as clearly and efficiently as possible.
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

# initialize variables
v_len = 0
for x in range(26):
    v_len = len(str(x))
    if x == 26:
        break
    elif (int(x) % 3 == 0) and (int(x) % 5 != 0):
        # the number is divisible by 3 but not by 5
        if v_len == 1:
            print("0" + str(x) + ":\t Fizz")
        else:
            print(str(x) + ":\t Fizz")
    elif (int(x) % 3 != 0) and (int(x) % 5 == 0):
        # the number is divisible by 5 but not by 3
        if v_len == 1:
            print("0" + str(x) + ":\t Buzz")
        else:
            print(str(x) + ":\t Buzz")
    elif (int(x) % 5 == 0) and (int(x) % 3 == 0):
        # the number is divisible by 3 and 5
        if v_len == 1:
            print("0" + str(x) + ":\t FizzBuzz")
        else:
            print(str(x) + ":\t FizzBuzz")
    else:
        if (int(x) % 5 != 0) and (int(x) % 3 != 0):
            # the number is not divisible by 3 and 5
            if v_len == 1:
                print("0" + str(x) + ":\t")
            else:
                print(str(x) + ":\t")
# End program