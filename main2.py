# Input: 10, 25, 15
# Output: 25
# Find the largest of three numbers


x, y, z = input("Values: ").split()

if (x >= y and x >= z):
    print(x)
elif(y >= x and y >= z):
    print(y)
else:
    print(z)