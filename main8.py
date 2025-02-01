# Input: 1234
# Output: 10  (1+2+3+4)

# Sum of all digits in a number

val = str((input("Get the sum : ")))
sum = 0

for i in val:
    sum += int(i)

print(sum)
