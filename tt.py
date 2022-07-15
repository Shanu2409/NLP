import tweepy
import matplotlib.pyplot as plt
from textblob import TextBlob
consumerKey = 'YyK2uanHAOvZxTbCamOy2cWqm'
consumerSecret = 'ciGQ8JdzdbqJYYADn2SJNWnYdzekOAQJWWcGXqtJLe3qHEEhKC'
accessToken = '1159048690247458817-MuYoRW9Be6vevXV2FXHb9VBVUcRYjn'
accessTokenSecret = 'E2T15NucMC3wg4ZNCJt8rcsHOHivS53JGv5m9d9hGgTS2'
auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

searchTerm = input("Enter Keyword/Tag to search about: ")
NoOfTerms = int(input("Enter how many tweets to search: "))

p_search = tweepy.Cursor(api.search_tweets, q=searchTerm, lang = "en").items(NoOfTerms)

# p_search = api.search_tweets('Dance+')

p = nu = ng = 0

for tweet in p_search:
  # print(tweet.text)
  ala = TextBlob(tweet.text)
  senti = ala.polarity
  if senti > 0:
    p = p + 1
  elif senti < 0:
    ng = ng + 1
  else:
    nu = nu + 1

print(p,ng,nu)
w = {'positive': p, 'negitive': ng, 'nuteral': nu}

fig , ax = plt.subplots()
ax.bar(w.keys(), w.values(), color='#7eb54e')
fig.autofmt_xdate() #auto alignment of x axis
plt.savefig('graph.png')
plt.title(searchTerm, fontstyle='italic',
          backgroundcolor='#F0F0EE', pad=10)
plt.show()