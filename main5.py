word = input("Tell the 5-letter word: ")
guess = input("Tell the 5-letter guess: ")

a_list = [0] * len(word)
word_counts = {}  

for i in range(len(word)):
    if word[i] == guess[i]:
        a_list[i] = 2
    else:
        if word_counts.get(word[i]) is not None:
            word_counts[word[i]] += 1
        else:
            word_counts[word[i]] = 1

    



print(word_counts)
print(a_list)