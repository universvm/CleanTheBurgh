import os
from tweepy import OAuthHandler, API

TWITTER_CONSUMER_KEY_ENV = 'TWITTER_CONSUMER_KEY'
TWITTER_CONSUMER_SECRET_ENV = 'TWITTER_CONSUMER_SECRET'
TWITTER_ACCESS_TOKEN_ENV = 'TWITTER_ACCESS_TOKEN'
TWITTER_TOKEN_SECRET_ENV = 'TWITTER_TOKEN_SECRET'
if not os.environ[TWITTER_CONSUMER_KEY_ENV] or not os.environ[TWITTER_CONSUMER_SECRET_ENV]\
        or not os.environ[TWITTER_ACCESS_TOKEN_ENV] or not os.environ[TWITTER_TOKEN_SECRET_ENV]:
    raise EnvironmentError('Twitter API codes are not set up properly')


class Twitter(object):
    def __init__(self):
        consumer_key = os.environ[TWITTER_CONSUMER_KEY_ENV]
        consumer_secret = os.environ[TWITTER_CONSUMER_SECRET_ENV]
        access_token = os.environ[TWITTER_ACCESS_TOKEN_ENV]
        token_secret = os.environ[TWITTER_TOKEN_SECRET_ENV]
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, token_secret)
        self.api = API(auth)

    def get_tweet(self, tweet_id):
        return self.api.get_status(tweet_id)

