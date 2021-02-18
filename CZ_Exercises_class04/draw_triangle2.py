# Isosceles triangle. Iso symmetrical triangle 3 lines only
# Triangle base size 5 starting with 1.
# initialize variables


v_triangle = 9
v_count = 1
v_string = ""

# v_triangle even => please enter an ODD base triangle and greater than 1

for y in range(1, int(v_triangle) + 1):
    if v_count % 2 != 0:
        v_string = v_count * "*"
        v_n_string = str.center(v_string,v_triangle, ' ')
        print(v_n_string)
    v_count += 1
