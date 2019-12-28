##from nltk.tokenize import sent_tokenize, word_tokenize
##
##example_text = 'It’s never been easier to learn whatever you need to know online. And it’s never been harder to wade through the hype and ads to figure out what’s important and what sources you can trust.'
##
##print(sent_tokenize(example_text))
##print(word_tokenize(example_text))


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_text = 'It’s never been easier to learn whatever you need to know online. And it’s never been harder to wade through the hype and ads to figure out what’s important and what sources you can trust.'

stop_words = set(stopwords.words("English"))
print(stop_words)
words = word_tokenize(example_text)
print(words)
filtered_text = []

for i in words:
   if i not in stop_words:
       filtered_text.append(i)


print(filtered_text)
