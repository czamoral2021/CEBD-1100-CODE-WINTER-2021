# Exercise 5
# (15 minutes)
# 	Create a new list with the first ten values of 2n
# 	Use the "pow" (power) function for this.
# pow(value, exponent)
# 2 pow 0 = 1, 2 pow 1 = 2, 2 pow 2 = 4, 2 pow 3 = 8
# Etc…
# 	The new list should look like (including 0):
# 	[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024

# Python pow() Function
#
# The pow() function returns the value of x to the power of y (xy).
# If a third parameter is present, it returns x to the power of y, modulus z.

# Example
# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):
#
# x = pow(4, 3)



# 	Create a new list with the first ten values of 2n
# 	Use the "pow" (power) function for this.

value_numbers_list = list(range(11))
print(value_numbers_list)
value_pow_list = []
CONST_POW = 2
v_pow = 0
for i in value_numbers_list:
    v_pow = pow(CONST_POW, i)
    print(CONST_POW)
    print(str(i), v_pow)
    value_pow_list.append(v_pow)
print("The list of power numbers")
print(value_pow_list)



