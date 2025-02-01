# Input: "listen", "silent"
# Output: True

# Check if two strings are anagrams

first_input = input("First string: ")
second_input = input("Second string: ")
num = 0

for i in range(len(first_input)):
    for j in range(len(second_input)):
        if (first_input[i]) == second_input[j]:
            num += 1
            continue
        
            
if (num == len(first_input)):
    print(True)

