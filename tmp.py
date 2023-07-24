len_word = {}
a = ["dog","racecar","car"]
for word in a:
    len_word[len(word)] = word

print(len_word[max(len_word)])