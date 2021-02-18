# list1 = ["A", "B"]
#
# list2 = list1
#
# print(list1)
# print(list2)
#
# list1[1] = "X"
# list2[1] = "W"
# print("--------------")
#
# print(list1)
# print(list2)
#===============================================#
# copy it is different

list1 = ["A", "B"]

list2 = list1.copy()

print(list1)
print(list2)

list1[1] = "X"
list2[1] = "W"
print("--------------")

print(list1)
print(list2)