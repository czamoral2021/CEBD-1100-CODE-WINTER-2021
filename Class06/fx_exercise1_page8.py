def get_max(val1, val2, val3):
    if val1 > val2:
        maxi = val1
    elif val2 > val3:
        maxi = val2
    else:
        max1 = val3
    return maxi

print(get_max(8, 5, 3))

###

def get_max2(n1, n2, n3):
    max_num = 0
    num_list = [n1, n2, n3]
    for i in num_list:
        if i < max_num:
            max_num = 1
    return max_num

