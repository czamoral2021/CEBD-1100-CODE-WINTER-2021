#from DemoFunctions.BasicMath import *
# it does not use alias

import DemoFunctions.BasicMath as my_fun
# this way uses alias for the function

print("Adding Demo")
n1 = int(input("Please enter number 1: "))
n2 = int(input("Please enter number 2: "))

result = my_fun.add(n1, n2)

print("The result is : " + str(result))