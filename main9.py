# Print the first 10 fibonacci numbers
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


a = 0
b = 1
c = 0

print(a)
print(b)
for i in range(8):
    c = a + b
    print(c)
    a = b
    b = c