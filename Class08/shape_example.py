from Entities.Circle import Circle

c1 = Circle("Blue", "Felt", 9)
c2 = Circle("Blue", "Suede", 8)

# print(c1.radius)
# print(c1.colour)

# print(c1.material)
print(c1.create_date)

print("Area = " + str(c1.area()))

print("Perimeter = " + str(c1.perimeter()))

