from flask import Flask
import nltk
import sys
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
      try:
        url = request.form['url']
        req = requests.get(url)

        # Setting up API Keys and Secrets
        apiConsumerKey = str(os.environ['CONSUMER_KEY'])
        apiConsumerSecret = str(os.environ['CONSUMER_SECRET'])
        apiAccessTokenKey= str(os.environ['ACCESS_TOKEN_KEY'])
        apiAccessTokenSecret = str(os.environ['ACCESS_TOKEN_SECRET'])

        # Get Request from Twitter API
        api = TwitterAPI(apiConsumerKey, apiConsumerSecret, apiAccessTokenKey,
				 apiAccessTokenSecret)
        query = '%23{0}'.format(req)
        before_results = api.request('search/tweets', {'q':query})
        results.append(before_results)

      except:
        errors.append(
          " Couldnt get request"
        )
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
