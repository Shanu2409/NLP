from textblob import TextBlob
import nltk
from newspaper import Article

url = 'https://www.geeksforgeeks.org/'
article = Article(url)

text = 'The Product was '
# print(text)

obj = TextBlob(text)

senti = obj.sentiment.polarity
print(senti)

if senti > 0:
  print("Positive")
elif senti < 0:
  print("Negative")
else:
  print("Neutral")