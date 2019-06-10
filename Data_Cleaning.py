import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text= "After sleeping for four hours, she decided to sleep another four hours."


#This part is for Tokenization

token=word_tokenize(text)

token


#This part is for Stop words


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

text1= "Anything you want here a the ! "

stop_words= set(stopwords.words('english'))

word_tokens=word_tokenize(text1)

filtered_sentence=[]

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)


#This part is to find Frequency distribution

from nltk.probability import FreqDist
fdist = FreqDist(word_tokens)
print(fdist)

fdist.most_common(3)

import matplotlib.pyplot as plt
fdist.plot(13,cumulative=False)
plt.show()


#This part is for Stemming

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize

s=PorterStemmer()

stemmed_words=[]

for w in filtered_sentence:
  stemmed_words.append(s.stem(w))
  
print(stemmed_words)  

