from flask import Flask
import nltk
import sys
sys.path.insert(0, '../')
import keys
keys.main() // Adds env variables for the API keys.

app = Flask(__name__)

sentence = "I love to eat spicy tacos, sip on coronas, all while relaxing at the beach."

@app.route('/', methods=["GET", "POST"])
def index():
    errors = []
    results = {}
    if request.method == "POST":
      try:
        url = request.form['url']
        r = requests.get(url)
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

