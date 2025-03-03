# a = {}
# print(type(a))

# b = set()
# print(type(b))

# def func1(*args):
#     for x in args:
#         print(x)

# func1("bcjh", "jdvb", "kfdnv")

# c = "Tanmay"

class Employee:
    name = "Tanmay"
    def __init__(self, value):
        self.value = value

    @classmethod
    def print_name(self):
        print(self.value)

    @staticmethod
    def print_hello():
        print("Hello")

emp1 = Employee("Tanmay")
emp1.print_name()

Employee.print_hello()