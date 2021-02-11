# empty list
# colours = []


# colours = ["red", "green", "blue", "yellow"]
#
# prime_numbers = [2,3,5,7,9,11,19]
# change the list after it's created.

# print(colours[1])
# 1 -> green

# Iterate over the list
# enumerate over the list
# for c in colours:
#     print(c)

# Every student has 2 grades available. A midterm grade and a final grade.
# These grades must be grouped together

grades = [70, 72, 80, 81, 66, 67]
grades_better = [
    [70,72],
    [80,81],
    [66,67]]

for s in grades_better:
    grade_midterm = s[0]
    grade_final = s[1]
    av = (grade_midterm + grade_final) / 2
    print(av)



