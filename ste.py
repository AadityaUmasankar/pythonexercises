from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_text = 'It’s never been easier to learn whatever you need to know online. And it’s never been harder to wade through the hype and ads to figure out what’s important and what sources you can trust.'

words = word_tokenize(example_text)

for i in words:
    print(ps.stem(i))

