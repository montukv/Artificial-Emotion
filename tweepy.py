import tweepy
from textblob import TextBlob

#  Authenticate of twitter account
consumer_key= 'Your consumer key '
consumer_secret= 'Your secret key'

access_token='your access token'
access_token_secret='your access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Retrieve Tweets
public_tweets = api.search('ajinkya')



for tweet in public_tweets:
    print(tweet.text)
    
    #Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("- ")
