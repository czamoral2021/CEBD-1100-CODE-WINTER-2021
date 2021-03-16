class Student:

    def __init__(self, fn, ln):

        self.first_name = fn
        self.last_name = ln

    def __str__(self):
        return self.first_name + " " + self.last_name


student1 = Student("Brendan", "Wood")

print(student1)




