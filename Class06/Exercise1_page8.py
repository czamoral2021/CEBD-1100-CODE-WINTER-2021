def get_max(val1, val2, val3):
    if val1 > val2:
        maxi = val1
    elif val2 > val3:
        maxi = val2
    else:
        maxi = val3
    return maxi


def get_max2(n1, n2, n3):
    max_num = 0
    num_list = [n1, n2, n3]
    for i in num_list:
        if i < max_num:
            max_num = i
    return max_num


def get_max3(n1, n2, n3):
    if n1 > n2 and n1 > n3: # If n1 is bigger than both, return right away
        return n1
    if n2 > n3:
        return n2
    return n3


print(get_max3(8, 9, 3))