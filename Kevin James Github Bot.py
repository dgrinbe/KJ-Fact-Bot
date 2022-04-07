'''
This code is used to post the actual thing
'''


import tweepy
from tweepy import OAuthHandler

import datetime
import csv
import pandas as pd


#API keys for accessing the Twitter dev app + the KJ bot
#do not allow anyone else to get access to your API verification info.


ACCESS_TOKEN = "******************-***********************"
ACCESS_TOKEN_SECRET = "*********************************"

API_key='********************'
API_secret='****************'


#get access permission from the Twitter API for the bot
auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api=tweepy.API(auth)



#getting today's date
current_time=datetime.datetime.now()
month=current_time.month
day=current_time.day


date=f'{month}/{day}'
date=f"['{date}']" #formatting the date into a string to match the values in the excel spreadsheet



#using pandas (pd) to pull up the twitter posts. Make sure you have your spreadsheet saved in the same folder/directory as this code
# I used an .xlsx (excel spreadsheet)


#getting the scheduled post dates from the excel spreadsheet
df=pd.read_excel('KJAS_github.xlsx',sheet_name=0,usecols="A")
post_date=df.values.tolist()


#getting the actual posts from the excel spreadsheet
df=pd.read_excel('KJAS_github.xlsx',sheet_name=0,usecols="B")
post_text=df.values.tolist()


#iterating through the list to see which fact to post today
i=0
while i< len(post_text):
    if date==(str(post_date[i])):
        post=str(post_text[i])
        print(type(post))
        post=post[2:-2] # remove str artifacts (this'll clean up your post text)
        api.update_status(post)
    i=i+1

