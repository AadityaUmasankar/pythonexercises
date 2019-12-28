import nltk

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer


train_text = state_union.raw('2005-GWBush.txt')
sample_text = state_union.raw('2006-GWBush.txt')

##print(sample_text)

##custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
##
##tokenized = custom_sent_tokenizer.tokenize(sample_text)

##print(tokenized)

tokenized = PunktSentenceTokenizer().tokenize(sample_text)

def process_control():
   try:
      for i in tokenized:
         words = nltk.word_tokenize(i)
         tagged = nltk.pos_tag(words)
         print(tagged)
   except Exception as e:
       print(str(e))

process_control()
