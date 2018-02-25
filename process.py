import json
import sys 
import os
sys.path.insert(0, '../')
import keys
from TwitterAPI import TwitterAPI
keys.main()

def main():
  # Parse Json API request from twitter to a list of actual tweets
  apiConsumerKey = str(os.environ['CONSUMER_KEY'])
  apiConsumerSecret = str(os.environ['CONSUMER_SECRET'])
  apiAccessTokenKey= str(os.environ['ACCESS_TOKEN_KEY'])
  apiAccessTokenSecret = str(os.environ['ACCESS_TOKEN_SECRET'])
  api = TwitterAPI(apiConsumerKey, apiConsumerSecret, apiAccessTokenKey, apiAccessTokenSecret)
  r = api.request('search/tweets', {'q':'%23curling'})
  for x in r:
    print(x)

#  j = json.load(example)
#  print(j[''])
#  print(example) 
  sys.exit()

if __name__ == "__main__":
  main()

  
