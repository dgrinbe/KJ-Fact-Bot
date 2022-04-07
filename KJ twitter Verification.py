'''
This code is used to link up a twitter acct with the twitter bot. You only need to run this once per twitter account. If you did everything right,
it should open your browser, and ask you to grantpermissions to the twitter bot.

You need ellevated twitter dev access for this to work for you.
'''

import tweepy
import webbrowser


#api keys + acct access token
ACCESS_TOKEN = "******************-***********************"
ACCESS_TOKEN_SECRET = "*********************************"

API_key='********************'
API_secret='****************'


#make a request to the Twitter Bot
auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api=tweepy.API(auth)

# this opens the actual link. Make sure you're connected to the browser
webbrowser.open(auth.get_authorization_url())

