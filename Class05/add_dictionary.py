provinces = {"QC": "Quebec", "ON": "Ontario"}

provinces["BC"] = "British Columbia"

print(provinces)

# How to delete BC

# del(provinces["BC"])

print(provinces)

for x in provinces:
    print(x)
    # print just the key

for x in provinces.items():
    print(x)
    # tuple each element with key and value

# for x in provinces.items():
#     print(x[0] + " is " + x[1])

for x, y in provinces.items():
    print(x + " is " + y)

for x in provinces.values():
    print(x)
    # print all dictionary values

for x in provinces.keys():
    print(x)
    # print all dictionary keys

print(provinces.keys())

print(provinces.values())

print("QC" in provinces)
print("XX" in provinces)

# another example

student_list = {1234567: "student1", 223456: "student2"}

# Dictionary does not work by position, it works by the key

product_garde = {1: "New", 2: "Used", 3: "Refurbished"}

print(product_garde[2])






