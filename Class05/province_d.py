provinces = {"QC": "Quebec", "ON": "Ontario"}

# fist part is considered key and must be unique

# provincelist = ["Quebec", "Ontario"]

print(provinces["QC"])

# print(provinces["XX"])
# # it does not exist and the results will be an error

print(provinces.get("QC"))

## better if the key does not exist

print(provinces.get("XX"))

# provincename = provinces.get("XX")
provincename = provinces.get("XX", "No province")

if provincename != None:
    print(provincename)
else:
    print("This province doesn't exist")
