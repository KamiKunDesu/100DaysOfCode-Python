import os
import tweepy

# Initialize secret ke  ys
TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_KEY_SECRET = os.environ['TWITTER_API_KEY_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# Initialize a client
client = tweepy.Client(consumer_key=TWITTER_API_KEY,
                       consumer_secret=TWITTER_API_KEY_SECRET,
                       access_token=TWITTER_ACCESS_TOKEN,
                       access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

response = client.create_tweet(text="Hey Twitter. This GitHub action is letting you know I just updated my repo: https://github.com/KamiKunDesu/100DaysOfCode-Python/")

print(response) 
                        