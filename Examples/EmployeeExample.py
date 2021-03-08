class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def __str__(self):
        return '{} {}'.format(self.first,self.last)

emp_1=Employee('Bassel','Kotaish',66000)
emp_2=Employee('Husam','kasem',32000)
emp_3=Employee('Hasan','Abas',67000)

print(emp_1)
print(emp_2)
print(emp_3)