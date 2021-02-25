base_size = input("Enter the size of the triangle base > ")
if not base_size.isnumeric():
    print("The amount must be a number, try again.")
    exit()
else:
    print("do something with amount entered")


#

if not float(base_size) % 1 == 0:
    print("The number isn't integer.")
    exit()

if not float(base_size) % 2 == 0:
    print("The number must be odd.")
    exit()

