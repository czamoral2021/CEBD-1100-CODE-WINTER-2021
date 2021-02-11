# Keep asking the user for a number (integer)
# keep track of the SUM of the numbers added
# When the user enters "-1" then stop and print the sum of all numbers entered

sum_of_numbers = 0
entered_value = ""

while True:
    entered_value = int(input("enter a number >"))
    if entered_value == -1:
        break
    else:
        sum_of_numbers += entered_value

print(f"The sum of the numbers is {sum_of_numbers}")


