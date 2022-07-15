from textblob import TextBlob
text = input("Enter a comment : ")
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