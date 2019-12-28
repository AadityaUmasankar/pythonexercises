from nltk.corpus import names
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

porter_stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()
##
##print (names.words()[:10])
##print(len(names.words()))

names_first10 = (names.words()[:10])

print(names_first10)

stem_list = []

for i in names_first10:
    j = porter_stemmer.stem(i)
    stem_list.append(j)

print(stem_list)

lemme_list = []

for i in stem_list:
    j = lemmatizer.lemmatize(i)
    lemme_list.append(j)

print(lemme_list)
    
