import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def analyze_sentiment(comment):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(comment)

    if sentiment_score['compound'] >= 0.05:
        return 'positive'
    elif sentiment_score['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'


comment = input("Enter your comment: ")
sentiment = analyze_sentiment(comment)
print("Sentiment:", sentiment)