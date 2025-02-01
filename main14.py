# Input: "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Count the frequency of each character in a string

val = input("Tell the input: ")
my_dict = {}

for i in range(len(val)):
    if my_dict.get(val[i]) is not None:
        my_dict[val[i]] += 1
    else:
        my_dict[val[i]] = 1

print(my_dict)
