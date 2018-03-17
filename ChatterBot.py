# Dependencies
import tweepy
import time
import datetime
import random
import pprint

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Twitter API Keys
consumer_key = "eyG6KeGTWnqxUcOncy0TnYpMy"
consumer_secret = "rL9e3qujzRVJNZnZPPqlXnqtMdenCgfx7IhfMzwToBY3dVqeYo"
access_token = "722089747959693312-SwMH8g2TNIvLog6W9mJbjFIX23u1z4Q"
access_token_secret = "7FS2b2i3UMoEvY1wAP2ncjJ78ZheunyhHK8JpIqBy3cPl"

# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# get the date in mm-dd formate
def getDate():
    now = datetime.datetime.now()
    date_string = now.strftime("%a %d %b %H:%M:%S %Y")
    #print(date_string)
    return date_string

# Create function for tweeting
def QuoteItUp(status):

    # Quotes to Tweet
    quote_list = [" sentiment is good for ",
            " sentiment is bad for "]
    # create the tweet text
    date_string = getDate()
    tweet_text = str(date_string) + quote_list[int(status)]
    print(tweet_text)
    # Tweet the next quote
    #api.update_status(tweet_text)

    # Print success message
    print("Tweeted successfully, sir!")

def getTweets(topic):
    found_tweets = []
    #07/03/08
    # Search for all tweets
    public_tweets = api.search(topic, count=10, result_type="recent")

    # Loop through all tweets
    for tweet in public_tweets["statuses"]:
        # put each tweets data into a dict
        tweet_dict = {}

        # Get ID and Author of most recent tweet directed to me
        tweet_dict['id'] = tweet["id"]

        tweet_dict['author'] = tweet["user"]["screen_name"]
        tweet_dict['text'] = tweet['text']

        # Print the tweet_id
        #print(tweet_dict['text'])

        #07/02/04
        # Run Vader Analysis on each tweet
        tweet_dict['sentiment'] = analyzer.polarity_scores(tweet_dict['text'])

        found_tweets.append(tweet_dict)
    return found_tweets

# Set timer to run every minute
counter = 0

while(counter < 10):

    current_status = random.uniform(0,1)
    tweets = getTweets('amd')
    QuoteItUp(current_status)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(tweets)
    counter+= 1
    time.sleep(300)
