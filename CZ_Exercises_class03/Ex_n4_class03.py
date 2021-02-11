# Restaurant Seating: Write a program that asks the user how many people are
# in their dinner group. If the answer is more than eight, print a message saying
# they’ll have to wait for a table. Otherwise, report that their table is ready.

# b. Ex_n4_class03

from string import digits

# initialize variables
num_of_users = 0
v_stay = True

# text = 'text%'
#
# from string import ascii_letters, digits
#
# if set(text).difference(ascii_letters + digits):
#     print('Text has special characters.')
# else:
#     print("Text hasn't special characters.")

while v_stay:
    num_of_users = input("How many people are in the dinner group, number please?>")
    if num_of_users == -1:
        print("You are not sure to eat in this restaurant")
        v_stay = False
    if str(num_of_users).isalpha() or set(str(num_of_users)).difference(digits):
        print("number of users is not an integer number")
    # if str(num_of_users).isalpha() or not str(num_of_users).isnumeric():
    #     print("number of users is not an integer number")
    else:
        if (int(num_of_users) <= 8) and (int(num_of_users) > 0):
            print(f"Your table is ready for {num_of_users} users")
            v_stay = False
        elif int(num_of_users) > 8:
            print("We do not have a table for more than 8 users")

