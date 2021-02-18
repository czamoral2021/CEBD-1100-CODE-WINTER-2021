# 1 Create a list with numbers 0 to 9 in it.
# 2 Display the list separated by comma (comma at the end ok)
# 3 Display all even elements of the list.
# 4 Display the average value of all elements in the list.

# 1 Create a list with numbers 0 to 9 in it.
list1 = list(range(10))
even_list1 = list(range(0,10,2))
even_list2 = []
# e.g.
print(range(10))
print(list1)

# e.g

# del(list1[4])

# 2 Display the list separated by comma (comma at the end ok)
for x in list1:
    print(str(x), end="")
    if x < max(list1):
        print(",", end="")

# 3 Display all even elements of the list.
for x2 in list1:
    if x2 % 2 == 0:    # even numbers
        even_list2.append(x2)
        print(x2)

# 4 Display the average value of all elements in the list.

print(sum(list1)/len(list1))

