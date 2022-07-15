import tweepy

consumer_key = 'YyK2uanHAOvZxTbCamOy2cWqm'
consumer_secret = 'ciGQ8JdzdbqJYYADn2SJNWnYdzekOAQJWWcGXqtJLe3qHEEhKC'
access_token = '1159048690247458817-MuYoRW9Be6vevXV2FXHb9VBVUcRYjn'
access_token_secret = 'E2T15NucMC3wg4ZNCJt8rcsHOHivS53JGv5m9d9hGgTS2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('bitcoin')
for tweet in public_tweets:
    print (tweet.text)
