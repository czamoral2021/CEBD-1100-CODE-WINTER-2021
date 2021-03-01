# Exercise 1
# (5 minutes)
# Your input will be:
# mylist2 = ['red', 'green', 'blue']
# 1. Add two colours to the end, 'black' and 'white'.
# 2. Change the third item to 'yellow'.
# 3. Delete the colour green by position.
# 4. Delete the colour red by name.
# 5. Make a for loop to print each remaining item, capitalized, with a line
# number in front of it.
# Exercise 1 - Output
# 1 Yellow
# 2 Black
# 3 White

# 1. Add two colours to the end, 'black' and 'white'.

mylist2 = ['red', 'green', 'blue']
mylist2 = mylist2 + ['black', 'white']
print(mylist2)

# 2. Change the third item to 'yellow'.
print()
mylist2[2] = 'yellow'
print(mylist2)

# 3. Delete the colour green by position.

# mylist2.remove('green'')  ## by value, but the first one found whn it is repeated

del(mylist2[1]) ## by position

print()
print(mylist2)

# 4. Delete the colour red by name.

mylist2.remove('red')
print()
print(mylist2)

# 5. Make a for loop to print each remaining item, capitalized, with a line
# number in front of it.

print()
y = 0
for x in mylist2:
    y += 1
    print(str(y), x.title())
