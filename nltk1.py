from sklearn.datasets import fetch_20newsgroups
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
import re
from nltk.tokenize import sent_tokenize, word_tokenize
text_data = fetch_20newsgroups()
print(type(text_data))
rw_text = text_data.data[:4]
rw_text = rw_text
One_text = []

def to_lower(data):
  for word in rw_text:
    One_text.append(str.lower(word))

to_lower(rw_text)

# print(One_text)

two_text = []

#list compression 
two_text = [word_tokenize(i) for i in One_text]

#regular expression to cleane the special char



three_text = []

for word in two_text:
  clean = []
  for w in word:
    res = re.sub(r'[^\w\s]',"",w)
    if res != "":
      clean.append(res)
  three_text.append(clean)

four_text = []

for words in three_text:
  w = []
  for word in words:
    if word not in stopwords.words('english'):
      w.append(word)
  four_text.append(w )

five_text = []

port = PorterStemmer()

for words in four_text:
  w = []
  for word in words:
    w.append(port.stem(word))
  five_text.append(w)


wnet = WordNetLemmatizer()

lem = []

for words in five_text:
  w = []
  for word in words:
    w.append(wnet.lemmatize(word))
  lem.append(w)

# print(lem)

p = 0
Nu = 0
Ng = 0

for words in lem:
  w = []
  for word in words:
    obj = TextBlob(str(word))
    senti = obj.sentiment.polarity

    if senti > 0:
      p +=  1
    elif senti < 0:
      Ng +=  1
    else:
      Nu +=  1
  

print("p = ", p, " neg = ", Ng, " nu = ", Nu)

x = {"Positive": p, "Negative": Ng, "Nuretral" : Nu}

fig , ax = plt.subplots()
ax.bar(x.keys(), x.values(), color='#123456')
fig.autofmt_xdate() #auto alignment of x axis
plt.savefig('g.png')
plt.title('Emotions found in life story of Nikola Tesla', fontstyle='italic',
          backgroundcolor='#F0F0EE', pad=10)
plt.show()