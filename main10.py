# Input: 5
# Output: 120 (5! = 5*4*3*2*1)

# Find factorial using loop


val = int(input("Find the factorial of : "))
mul = 1

for i in range(val):
    mul *= (i+1)

print(mul)