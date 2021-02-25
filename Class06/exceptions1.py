## x = 5 / 0

# raise Exception("The credit card requires 16 digits")

def divide_numbers(n1:float, n2:float):
    result = 0
    try:
        result = n1 / n2
        return result
    except:
        return False

# print(divide_numbers(7,6))

print(divide_numbers(7,0))



