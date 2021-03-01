# Exercise 2
# (20 minutes)
# Create a list of 20 numbers, randomly assigned.
# To generate the list, we can use:
# random_list = [random.randrange(1, 100) for i in range(20)]
# Scan the list and display several values using a manual method:
# 	The minimum, the maximum, the count and the average.

import random

# Minimum, Maximum, Average, Sum


# Maximum manually

random_list = [random.randrange(1, 100) for i in range(20)]
print(random_list)


max_num = 1
for i in random_list:
    print(str(max_num), i)
    if i > max_num:
        max_num = i
print("The Max value is : " + str(max_num))

# Minimum manually

min_num = 100
for i in random_list:
    print(str(min_num), i)
    if min_num > i:
        min_num = i
print("The Min value is : " + str(min_num))

# Average manually
v_count = 0
avg_num = 0
v_sum = 0
for i in random_list:
    v_count += 1
    print(str(i), v_count)
    if v_count == 1:
        v_sum = i
    else:
        v_sum = v_sum + i
        print(v_sum)
        avg_num = v_sum/v_count
print(f"The Average value is : {avg_num}")

# Sum manually
v_count = 0
v_sum = 0
for i in random_list:
    v_count += 1
    print(str(i), v_count)
    if v_count == 1:
        v_sum = i
    else:
        v_sum = v_sum + i
        print(v_sum)
print(f"The Total value is : {v_sum}")
