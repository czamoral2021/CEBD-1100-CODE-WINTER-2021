# Exercise 5
# (10 minutes)
# Make a function that takes up to 3 arguments and returns a list of 1, 2 or 3 items
# (an array).

def func_until3_arguments(num_arg=0, arg_1="", arg_2="", arg_3=""):
    # print("Arg # 1 is " + arg_1)
    # print("Arg # 2 is " + arg_2)
    # print("Arg # 3 is " + arg_3)
    if num_arg == 1:
        v_list = [arg_1]
        print(v_list)
    elif num_arg == 2:
        v_list = [arg_1, arg_2]
        print(v_list)
    elif num_arg == 3:
        v_list = [arg_1, arg_2, arg_3]
        print(v_list)
    else:
        print("function works between 1 and 3 arguments")


func_until3_arguments(1,"Jack")

func_until3_arguments(2,"Jack", "Cat")

func_until3_arguments(3,"Jack", "Cat", "Montreal")

## with wrong paramaters
print()

func_until3_arguments(0,"Jack")

func_until3_arguments(3,"Jack", "Cat")

func_until3_arguments(4,"Jack", "Cat", "Montreal")




