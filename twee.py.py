import tweepy
from textblob import TextBlob

# Step 1 - Authenticate of user
consumer_key= 'Your consumer key '
consumer_secret= 'Your secret key'

access_token='your access token'
access_token_secret='your access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('ajinkya')



for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("- ")
