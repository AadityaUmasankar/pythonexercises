
sentence = " I love the fucking hell out of the blue sky"

word_dict = {}

for word in sentence.split():
    word_dict.setdefault(word,0)
    word_dict[word] += 1

print(word_dict)
