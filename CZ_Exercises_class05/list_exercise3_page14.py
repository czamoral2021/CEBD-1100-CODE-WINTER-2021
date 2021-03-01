# Exercise 3
# (10 minutes)
# Create a list of 20 numbers, randomly assigned.
# To generate the list, we can use:
# random_list = [random.randrange(1, 100) for i in range(20)]
# Repeat exercise 2 using the built-in functions.
# 	Use the “min”, “max”, “len” and “sum” functions.


import random

# Minimum, Maximum, Average, Sum

random_list = [random.randrange(1, 100) for i in range(20)]

print(random_list)
v_min = min(random_list)
v_max = max(random_list)
v_sum_values = sum(random_list)
v_len_list = len(random_list)
print(v_len_list)
# total items in the list
v_avg_values = sum(random_list)/v_len_list
print()

print("The Min value is : " + str(v_min))
print("The Max value is : " + str(v_max))
print("The Average value is : " + str(v_avg_values))
print("The Sum of values is : " + str(v_sum_values))