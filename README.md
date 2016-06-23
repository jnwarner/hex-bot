# Hex Bot
Python script to tweet a random hex code when the script runs.

# Setup
Download the Tweepy library using `pip install tweepy`

Create a new application on [apps.twitter.com](http://apps.twitter.com)

Copy the consumer key, consumer key secret, authorization token, and authorization token secret.

Enter these into their respective variables in a new file named `secrets.py`

```python
C_KEY = "" 
C_SECRET = ""
A_TOKEN = ""
A_TOKEN_SECRET = ""
```

Now run the python script with the proper credentials in the `secrets.py` file imported into the `bot.py` file.

### Easy as that!
This can be uploaded to a server and set on a crontab to run the script periodically. Make sure you don't upload the `secrets.py` file, that has all your twitter credentials!
