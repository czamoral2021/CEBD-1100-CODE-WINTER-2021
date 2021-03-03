# Exercise 4
# (10 minutes)
# 1. Create a function that received a list as a parameter. The function should
# print the list items one over the other.
# 2. Modify the previous function to get a title, and use the supplied title as the
# title of your list.
# ******************************************************************************************************
# ******************************************************************************************************
#
#
# 1. Create a function that received a list as a parameter. The function should
# print the list items one over the other.


CONST_RANGE = 11
v_list = list(range(CONST_RANGE))


def func_list_parameters(v_list:list):
    for i in v_list:
        print(v_list[i], end="\n")
    return print(v_list)


l1 = v_list
func_list_parameters(l1)
print()

# 2. Modify the previous function to get a title, and use the supplied title as the
# title of your list.


v_title = input("Enter list title please > ")
v_title = v_title.upper()


CONST_RANGE1 = 11
v_list1 = list(range(CONST_RANGE1 + 1))
print(v_list1)


def func_list_parameters1(v_list1:list):
    v_list1[0] = v_title
    print(v_list1[0], end="\n")
    i = 1
    while i < CONST_RANGE + 1:
        print(v_list1[i], end="\n")
        i += 1
    return print(v_list1)


l2 = v_list1
func_list_parameters1(l2)
print()


