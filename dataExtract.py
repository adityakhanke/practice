import csv
import pandas as pd
import nltk
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
import string

tokenizer = TweetTokenizer()
stopwords_english = stopwords.words('english')

file = 'Edumantra.csv'

data = pd.read_csv(file)
video_title = list(data['video_title'])

vocab = []
hash = []
for title in video_title:
    words = tokenizer.tokenize(title)
    for word in words:
        word = word.lower()
        if word[0]=='#':
            hash.append(word)
        else:
            if word not in stopwords_english and word not in string.punctuation:
                if word not in vocab:
                    vocab.append(word)

# vocab = vocab - hash

print(len(vocab))
print(vocab)
print(hash)
