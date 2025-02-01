# Input: "madam"
# Output: True

# Check if a string is palindrome or not

val = input("Check if it is palindrome or not: ")

def isPalindrome():
    for i in range(len(val)):
        if val[i] == val[-(i+1)]:
            continue
        else:
            return False
    return True

print(isPalindrome())