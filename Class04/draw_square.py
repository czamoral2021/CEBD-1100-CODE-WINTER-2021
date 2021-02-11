# ask the user how big the square should be, then draw the square.
# Use *2* methods to do this. (1) Using nested loops, (2) using the multiplication symbol.
# Use the "#" character to draw the square.

size = int(input("What is the size of your square?"))

# Method 1

for y in range(0, size):
    for x in range (0, size):
        print("%", end="")
    print()

# Method 2

for x in range(0, size):
    print("#" * size)

# At home draw a triangule


