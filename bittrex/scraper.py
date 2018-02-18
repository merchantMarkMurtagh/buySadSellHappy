import tweepy
import json
import requests
from bittrex.bittrex import Bittrex
import bittrexAPI as btx


consumer_key = ''
consumer_secret = ''
access_token = '-'
access_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Tweets
# for trends in api.search(q ="Ethereum", lang = "en", count= 100, show_user = False):
# 	print("________________________________")
# 	print(trends.text)
# 	print("\n")

# Bittrex

btx.getBalances()