import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'VfRpuuTl7crBJFvQRKZLQrVO0'
consumer_secret= 'oA2GMbCFkAVR5SYQRwjbMpLJrfPi1IOnBKJZmNT2bBfBZ5XgB7'

access_token='1125289565017608193-ZkXwHbVRf16jsN2maPOGryLyFMMIGZ'
access_token_secret='OvR6t3Jvkdy82LIXFY4FoVbPdGVSsV8Dx0jhPwl5FCZ15'

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