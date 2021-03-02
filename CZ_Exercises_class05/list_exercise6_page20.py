# Exercise 6
# (10 minutes)
#  Given an input list:
#  mylist = ["A", "B", "C"]
# 1. Create a new list "copied_list_1" by copying the list by assignment (a =
# b).
# 2. Create a new list "copied_list_2" by copying the list with the deep copy
# operator (x.copy) or the (":") operator.
# 3. In the original my_list, change "B" to "X".
# 4. Display both lists using the "print" command

# ********************************************************************************************************
# ********************************************************************************************************

# 1. Create a new list "copied_list_1" by copying the list by assignment (a =
# b).

mylist = ["A", "B", "C"]
#
copied_list_1 = mylist
print(copied_list_1)
print("point1")

# 2. Create a new list "copied_list_2" by copying the list with the deep copy
# operator (x.copy) or the (":") operator.

# Use "copy", or create a new list with the ":" rang
# newList = oldList[:]
# newList = oldList.copy()

copied_list_2 = mylist.copy()
print(copied_list_2)
print("point2 with copy method")
copied_list_2 = mylist[:]
print(copied_list_2)
print("point2 with range [:]")

# 3. In the original my_list, change "B" to "X".

mylist[1] = 'X'
print(mylist)
print("point3")

# 4. Display both lists using the "print" command

print(copied_list_1)
print(copied_list_2)
print("point4")

# mylist and copied_list_1 are the same in the memory

