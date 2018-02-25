# TrendLore

Get statistical data + graphs from Twitter according to #hashtag (Population size representative of the past 7 days)

http://trendlore.org

### Prerequisites
> Python Version: 3.6.3

![](https://i.imgur.com/NE6ie27.png)

Before you start the flask app you have to set your 
Enviorment Variables. start.py looks for a file to 
run called "keys.py" which should be a diractory above
the project working directory. 
Environmen Variables needed:

```
$CONSUMER_KEY
$CONSUMER_SECRET
$ACCESS_TOKEN_KEY
$ACCESS_TOKEN_SECRET
```

To get the flask app up and running you need to do:

```
$ source env/bin/activate

$ pip install -r requirements.txt
```

Next you need to enter the command to start up the server

```
FLASK_APP=start.py flask run
```

## Built With

❤️ @ HackCU IV: 2018 🕴

by:

* **Sal Camara** - Initial work - [sal2993](https://github.com/sal2993)
* **hexphase** - Initial work - [hexphase](https://github.com/hexphase)
* **Dong Lee** - Inital work - [dlee67](https://github.com/dlee67)

## License / Disclaimer

This project is licensed under the 2-clause BSD license. (See LICENSE.md)
