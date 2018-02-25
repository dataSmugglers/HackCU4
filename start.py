from flask import Flask
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
        url = request.form['url']

        print("Made it here")
        # Setting up API Keys and Secrets
        apiConsumerKey = str(os.environ['CONSUMER_KEY'])
        apiConsumerSecret = str(os.environ['CONSUMER_SECRET'])
        apiAccessTokenKey= str(os.environ['ACCESS_TOKEN_KEY'])
        apiAccessTokenSecret = str(os.environ['ACCESS_TOKEN_SECRET'])

        # Get Request from Twitter API
        api = TwitterAPI(apiConsumerKey, apiConsumerSecret, apiAccessTokenKey,
				 apiAccessTokenSecret)
        query = '%23{0}'.format(url)
        before_results = api.request('search/tweets', {'q':query})
        for i in before_results:
          results.append(i)
        results.append(before_results)

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
