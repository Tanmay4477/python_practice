class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, different):
        return Number(self.value + different.value)
    
    def __sub__(self, different):
        return Number(self.value - different.value)

n1 = Number(10)
n2 = Number(20)
n3 = n1 - n2  # Calls __add__
n4 = n1 - n2
print(n4.value)  # Output: 30
