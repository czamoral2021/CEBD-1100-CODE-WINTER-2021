# Print a list of even numbers from x to y

LIST_START = 1
LIST_END = 100

for n in range(LIST_START, LIST_END + 1):
    if n % 2 == 0:
        print(n)

    # if x == 101:
    #     break
    # elif int(x) % 2 == 0:
    #     print(str(x) + " is an even number")
    # else:
    #   continue