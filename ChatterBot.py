# Dependencies
import tweepy
import time

# Twitter API Keys
consumer_key = "eyG6KeGTWnqxUcOncy0TnYpMy"
consumer_secret = "rL9e3qujzRVJNZnZPPqlXnqtMdenCgfx7IhfMzwToBY3dVqeYo"
access_token = "722089747959693312-SwMH8g2TNIvLog6W9mJbjFIX23u1z4Q"
access_token_secret = "7FS2b2i3UMoEvY1wAP2ncjJ78ZheunyhHK8JpIqBy3cPl"

# Quotes to Tweet
quote_list = [
    "Quote 1.1",
    "Quote 2",
    "Quote 3"]


# Create function for tweeting
def QuoteItUp(quote_num):

    # Twitter credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Tweet the next quote
    api.update_status(quote_list[quote_num])

    # Print success message
    print("Tweeted successfully, sir!")


# Set timer to run every minute
counter = 1

while(counter < len(quote_list)):
    QuoteItUp(counter)
    counter+= 1
    time.sleep(60)
