# Write a program which uses nested loops to create a multiplication table.
# Use tabs (escape them) to achieve placement.
# Use formatting to format numbers if necessary
# Output table
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

# initialize variables

TABLE_TITLE = "\t \t \t Multiplication Table"
TABLE_SUBTITLE_1 = "\t \t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9"
TABLE_SUBTITLE_2 = "-------------------------------------------"
v_size = 9
v_len = 0
v_len_previous = 0
v_calc = 0
print(TABLE_TITLE)
print(TABLE_SUBTITLE_1)
print(TABLE_SUBTITLE_2)

for y in range(1, v_size + 1):
    print(str(y) + " | \t ", end="")
    for x in range(1, v_size + 1):
        v_calc = y * x
        v_len = len(str(v_calc))
        if v_len == 1 and x == 1:
            print(str(v_calc) + "", end="")
        elif v_len == 1 and v_len_previous == 1:
            print(str("   " + str(v_calc)), end="")
        elif v_len == 2 and v_len_previous == 1:
            print(str("  " + str(v_calc)), end="")
        elif v_len == 2 and v_len_previous == 2:
            print("  " + str(v_calc), end="")
        v_len_previous = v_len
    print()
