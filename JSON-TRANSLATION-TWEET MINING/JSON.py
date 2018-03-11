import json
import urllib
import requests
from bs4 import BeautifulSoup
from googletrans import Translator
#from tweepy import OAuthHandler
#from tweepy import API
#from tweepy import Cursor
from twitter import Twitter, OAuth, Twitter Stream #http://socialmedia-class.org/twittertutorial.html

def load(filename):
    json_string = filename
    parsed_json = json.loads(json_string)
    strs = []
    strs.append(parsed_json['title'])
    strs.append(parsed_json['text'])
    strs.append(parsed_json['source'])
    return strs

def translatelinks(title):

    arr = []
    translator = Translator()
    titletrans = translator.translate(title, dest = 'es')
    url = 'https://www.google.co.uk/search?q=' + titletrans
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    for x in range (0,9)
        link = soup.findNext('cite')
        arr.append(link)
    return arr

def getTweet(strlink):

    consumer_key = ""
    consumer_secretkey = ""
    access_token = ""
    access_tokensecret = ""

    oauth = OAuth(consumer_key,consumer_secretkey, access_token, access_tokensecret)
    twitter_stream = TwitterStream(auth=oauth)
    iterator = twitter_stream.statuses.sample()
    tweet_count = 1
    for tweet in iterator:
        tweet_count += -1
        return json.dumps(tweet).text #.text?
    if tweet_count <= 0:
        break




    #transtitle = parsed_json2['title']
    #translator.translate(transtitle)

