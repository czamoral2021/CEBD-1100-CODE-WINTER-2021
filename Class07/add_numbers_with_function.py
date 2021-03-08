#from DemoFunctions.BasicMath import *
# it does not use alias

#from DemoFunctions.BasicMath import *

import DemoFunctions.BasicMath as m
import DemoFunctions.DemoFile as x

# this way use alias fro each function


print("Adding Demo")
n1 = int(input("Please enter number 1: "))
n2 = int(input("Please enter number 2: "))

result = m.add(n1, n2)


print("The result is : " + str(result))


print(x.DemoFcn1())