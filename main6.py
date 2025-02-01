# Reverse a given string

# Input: "hello"
# Output: "olleh"

val = input("Give the input: ")

new_val = []

for i in range(len(val)):
    new_val.append(val[-(i+1)])

string = ''.join(new_val)

print(string)