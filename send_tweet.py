from twitter_keys import TWITTER_API_KEY, TWITTER_API_KEY_SECRET, TWITTER_BEARER_TOKEN, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET
import tweepy

# Initialize a client
client = tweepy.Client(consumer_key=TWITTER_API_KEY,
                       consumer_secret=TWITTER_API_KEY_SECRET,
                       access_token=TWITTER_ACCESS_TOKEN,
                       access_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

response = client.create_tweet(text="hello world! I'm testing this out with the Twitter API!")

print(response)


