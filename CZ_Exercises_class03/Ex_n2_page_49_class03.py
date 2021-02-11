# Exercise - 2 - page 49
# Using for and continue or break, print a list of even numbers from 1 to 100.
# Reminder: To see if a number is even, if the modulus of 2 is 0 then it is even (x
# % 2 == 0).

for x in range (1,101):
    if x == 101:
        break
    elif int(x) % 2 == 0:
        print(str(x) + " is an even number")
    else:
        continue




