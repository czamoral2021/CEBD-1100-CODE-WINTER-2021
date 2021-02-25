#
def is_numeric(n):
    try:
        float(n)
        return True
    except:
        return False

try:

    if not is_numeric(6.2):
        print("This number is not numeric.")
    else:
        print("The number IS numeric.")


    print(isinstance(7.1, float))
    # True or False

except:

    print("An error has occurred.")