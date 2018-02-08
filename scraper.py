import tweepy
import json

consumer_key = '1Z0mxhdSBmRoS6FPE04VRKxGt'
consumer_secret = 'bE2TIXle3yTTyYdaIkBOohYQGtzBglz9lXrZzaoo6FRPczTkm3'
access_token = '362553785-kR1F4B9VZswfVv1Ut8ZRzym31mJo2WE7s8lqyH0l'
access_secret = 'qbbo87lt3RvBZyWNOfAY1HdCDZxxfZ53msdFgy6XUluC6'
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

for trends in api.search(q ="$AMZN", lang = "en", count= 100, show_user = False):
	print("________________________________")
	print(trends.text)
	print("\n")
