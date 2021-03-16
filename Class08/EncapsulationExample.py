class Student:

    def __init__(self, fn, ln):

        self.first_name = fn
        self.last_name = ln
        # self.full_name = self.first_name + " " + self.last_name
        # breaking encapsulation rule, you cannot mix function with data, or calculations in __init__

    def full_name(self):
        return self.first_name + " " + self.last_name


student1 = Student("Brendan", "Wood")

print(student1.full_name())

student1.last_name = "Jones"

print(student1.full_name())
