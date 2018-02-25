from flask import Flask
import sys
sys.path.insert(0, '../')
import keys
app = Flask(__name__)

keys.main()

@app.route("/")
def welcome():
    return "- Welcome to TrendLore.org -"
