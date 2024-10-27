# Inheritance

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def display(self):
#         print(f"The name of Employee {self.id} is {self.name} ")
#
#
# # Showing inheritance
# class Student(Employee):
#     def display(self):
#         print(f"The name of student {self.id} is {self.name}")
#
# e = Employee("Shubhi", 1)
# e.display()
#
# s = Student("Somi",2)
# s.display()


# Access modifier
class Numbers:
    def __init__(self,a):
        self.__a = a

    # private is made using double underscore
    def display(self):
        print(f"Value of a is: {self.__a}")

    # protected is made using single underscore
    def _display(self): # protected method
        print(f"The value of a squared is: {self.__a*self.__a}")

obj = Numbers(10)
# print(obj.a)        # Can't access this as a is private
obj.display()
print(obj._Numbers__a)  # Name mangling
obj._display()  # using the protected method