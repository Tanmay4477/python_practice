word = input("Tell the 5 word: ")
guess = input("Tell the 5 guess: ")

a_list = []

for i in range(len(word)):
    if word[i] == guess[i]:
        a_list.append(2)
    elif guess[i] in word and word[i] != guess[i] and guess[i] in word != word[i]:
        a_list.append(1)
    else:
        a_list.append(0)

print(a_list)