from flask import Flask
import json
import parse
import nltk
import sys
from TwitterAPI import TwitterAPI
import os
import requests
from flask import Flask, render_template, request
sys.path.insert(0, '../')
import keys
keys.main() # Adds env variables for the API keys.

app = Flask(__name__)

sentence = "I love to eat spicy tacos, sip on coronas, all while relaxing at the beach."

@app.route('/', methods=["GET", "POST"])
def index():
    results = []
    errors = []
    if request.method == "POST":
        url = parse.remove_pound(request.form['url'])

        # API set up
        api = Twitter_API_Call()

        # Formating to search Hashtags
        query = '%23{0}'.format(url)

        # Actual API request
        before_results = api.request('search/tweets', {'q':query, 'count':100})

        print(str(before_results))

        # Count Posts and Concatenate posts
        post_tuple = parse_tweets(before_results)
        print(str(post_tuple))

        # dictionary mapping words to frequency of that word
        word_dict = parse.count_each_word(post_tuple[0])
        print(str(word_dict))

        # Sorted by frequency and returns two lists
        ordered_lists = parse.order_list(word_dict)
        print(str(ordered_lists))



    return render_template('index.html', errors=errors, results=results)


@app.route('/tokenize')
def tokenize():
    tokens = nltk.word_tokenize(sentence)
    return str(tokens)

@app.route('/tag')
def tag():
    tokens = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(tokens)
    return str(tags)

# Return a Concatonated String of Tweets
# Also returns number of tweets
def parse_tweets(dict_twitter):
  # Count our tweets
  count = 0
  cat = ""
  for i in dict_twitter:
    count = count +1
    cat += i["text"]
    cat += " "
  return (cat, count)
  
def Twitter_API_Call():
  apiConsumerKey = str(os.environ['CONSUMER_KEY'])
  apiConsumerSecret = str(os.environ['CONSUMER_SECRET'])
  apiAccessTokenKey= str(os.environ['ACCESS_TOKEN_KEY'])
  apiAccessTokenSecret = str(os.environ['ACCESS_TOKEN_SECRET'])

  # Get Request from Twitter API
  api = TwitterAPI(apiConsumerKey, apiConsumerSecret, apiAccessTokenKey,
                           apiAccessTokenSecret)
  return api
