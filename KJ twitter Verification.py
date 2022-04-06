'''
This code is used to link up a twitter acct with the twitter bot.
'''

import tweepy
import webbrowser



ACCESS_TOKEN = "******************-***********************"
ACCESS_TOKEN_SECRET = "*********************************"

API_key='********************'
API_secret='****************'


#make a request to the Twitter Bot
auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api=tweepy.API(auth)
# the first time
webbrowser.open(auth.get_authorization_url())

