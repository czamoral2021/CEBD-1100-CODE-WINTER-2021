# [QUESTION 2] MULTIPLICATION TABLE.
#
# Create a multiplication table, using “print” commands in Python, based on the input of the user.
# The program should ask: “What size multiplication table would you like printed? >”.
# If the user enters 10, then we should see values on each axis from 1 to 10 inclusive.
# Tips:
# 1. Use string formatting to give yourself fixed-size columns.
# 2. This will require at least two “for” statement to accomplish.
# 3. Avoid using a “while” loop here.
# A value of NINE (9) would render:

#           Multiplication Table
#       1   2   3   4   5   6   7   8   9
# ---------------------------------------
# 1 |   1   2   3........................
# 2 |   2   4   6........................
# 3 |   3   6   9........................
# 4 |   4   8  12........................
# 5 |   5  10  15........................
# 6 |   6  12  18........................
# 7 |   7  14  21........................
# 8 |   8  16  24........................
# 9 |   9  18  27........................

# The Multiplication table size is variable according with the user input, but
# this program has been designed to work with a minimum table size 1 and maximum table size 10
#
# This program will use a While loop to ask and validate the Multiplication table size only.
# For the Multiplication table output will use 2 nested For loops, and for the Table header a single For loop.

# initialize variables and constants

TABLE_MIN = 1
TABLE_MAX = 10
TABLE_TITLE = "\t \t \t Multiplication Table"
TAB_SUBTITLE_1 = "\t \t "
TAB_SUBTITLE_2 = "----------"
CONST_SUBTITLE_2 = 4
v_calc = 0
v_size = ""
v_subtitle_1 = ""
v_subtitle_2 = "-"
w_1 = ""
h_1 = ""
while v_size != "s":
    v_size = input("What size multiplication table would you like printed?(enter \"S or s\" to stop)>")
    if v_size[0:1].upper() == "S":
        break
    elif not v_size.isnumeric():
        print("Table size is not an integer number")
    else:
        if TABLE_MIN <= int(v_size) <= TABLE_MAX:
            # printing the table name
            for z in range(1, int(v_size) + 1):
                if z == TABLE_MIN:
                    v_subtitle_1 = TAB_SUBTITLE_1 + str(z) + ""
                    v_subtitle_2 = TAB_SUBTITLE_2
                elif z < TABLE_MAX:
                    v_subtitle_1 = v_subtitle_1 + "   " + str(z)
                    v_subtitle_2 = v_subtitle_2 + CONST_SUBTITLE_2 * "-"
                else:
                    v_subtitle_1 = v_subtitle_1 + "  " + str(z)
                    v_subtitle_2 = v_subtitle_2 + CONST_SUBTITLE_2 * "-"
            print(TABLE_TITLE)
            print(v_subtitle_1)
            print(v_subtitle_2)
            for y in range(1, int(v_size) + 1):
                # formatting the left column as an index for each row
                w_1 = "\t"
                print("{0:2} | {1}".format(y, w_1), end="")
                # calculation
                for x in range(1, int(v_size) + 1):
                    v_calc = y * x
                    if x == TABLE_MAX and y == TABLE_MAX:
                        print("{0:2}".format(v_calc))
                    elif x == (TABLE_MAX - 1) and y == TABLE_MAX:
                        h_1 = " "
                        print("{0:2}{1}".format(v_calc, h_1), end="")
                    else:
                        h_1 = "\t"
                        print("{0:2} {1}".format(v_calc, h_1), end="")
                print()
        else:
            print(f"Table size issues, please between {TABLE_MIN} and {TABLE_MAX}")