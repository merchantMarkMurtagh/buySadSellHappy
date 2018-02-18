import json
import requests
from bittrex.bittrex import Bittrex

apiKey = "495c5ae77cc84f8aa461f2cfa7400f64"

def prettyPrint(marketDict):
	for i in marketDict:
		print (i["MarketCurrencyLong"] + " | " + str(i["MinTradeSize"]))

def getMarket():
	URL = "https://bittrex.com/api/v1.1/public/getmarkets"
	resOb = requests.get(url = URL)
	resDict = resOb.json()
	res = resDict["result"]
	prettyPrint(res)

def getSummary():
	URL = "https://bittrex.com/api/v1.1/public/getmarketsummaries"
	resOb = requests.get(url = url)
	resDict = resOb.json()
	res = resDict["result"]

