# Triangle base size 5 starting with 1.
# Right sided triangle
# initialize variables

v_triangle = 5
v_count = 1

for y in range(1, int(v_triangle) + 1):
    print("*" * v_count)
    # v_count = v_count - 1
    v_count += 1