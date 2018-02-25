# TrendLore
Devs: Sal, NickName, HexMan
Get statistical data from Twitter by #hashtag
Python Version: 3.6.3

![](https://i.imgur.com/NE6ie27.png)

Before you start the flask app you have to set your 
Enviorment Variables. start.py looks for a file to 
run called "keys.py" which should be a diractory above
the project working directory. 
Environmen Variables needed:

$CONSUMER_KEY
$CONSUMER_SECRET
$ACCESS_TOKEN_KEY
$ACCESS_TOKEN_SECRET


To get the flask app up and running you need to do:

```
$ source env/bin/activate

$ pip install -r requirements.txt
```

Next you need to enter the command to start up the server

```
FLASK_APP=start.py flask run
```
