import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

text= "After sleeping for four hours, she decided to sleep another four hours."

#This part is for tokenization
token=word_tokenize(text)

token

#This part is for stop words
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

