# Input: [10, 5, 20, 8, 15]
# Output: 15

# Find the largest number in the list

user_input = input("Tell me the input: ").split()

your_input = list(map(int, user_input))

print(your_input)
j = 0
k = 0

for i in your_input:
    if i >= j:
        k = j
        j = i
    # elif i > k and i < j:
    #     k = i
    #     print("semen")
    

print(k)