class TestClass:

    common_value = "X"

    def __init__(self, name):
        self.name = name

obj1 = TestClass("Brendan")
obj2 = TestClass("Mary")

print(obj1.common_value)

TestClass.common_value = "Y"

print(obj1.common_value)