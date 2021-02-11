# Keep asking the user for a number (integer)
# keep track of the SUM of the numbers added
# When the user enters "-1" then stop and print the sum of all numbers entered

sum_of_numbers = 0
entered_value = ""

while entered_value != -1:
    entered_value = int(input("enter a number>"))
    if entered_value != -1:
        sum_of_numbers += entered_value

# print("The sum of the numbers is {}".format(sum_of_numbers))
print(f"The sum of the numbers is {sum_of_numbers}")

