import json
import requests
import time
import hashlib
from bittrex.bittrex import Bittrex

# all requests made using GET
API_KEY = "495c5ae77cc84f8aa461f2cfa7400f64"

def prettyPrint(marketDict):
	for i in marketDict:
		print (i["MarketCurrencyLong"] + " | " + str(i["MinTradeSize"]))

def printBalances(balanceDict):
	print(balanceDict)
	#print(i["Currency"] + " | " + str(i["Balance"]))

def getMarket():
	URL = "https://bittrex.com/api/v1.1/public/getmarkets"
	resOb = requests.get(url = URL)
	resDict = resOb.json()
	res = resDict["result"]
	prettyPrint(res)

def getSummary():
	URL = "https://bittrex.com/api/v1.1/public/getmarketsummaries"
	resOb = requests.get(url = URL)
	resDict = resOb.json()
	res = resDict["result"]

def getBalances():
	nonce = time.time()
	hshM = hashlib.sha512()
	URL = "https://bittrex.com/api/v1.1/account/getbalances?apikey=" + API_KEY + "&nonce=" + str(nonce)
	resDict = (requests.get(url= URL)).json()
	print(resDict)
	printBalances(resDict["result"])


def buyOrder(market, quantity, rate):	
	URL = "https://bittrex.com/api/v1.1/market/buylimit?apikey=" + API_KEY +"&market="+ market +"&quantity=" + quantity + "&rate="+ rate
	resDict = (requests.get(url = URL)).json()
	successfull = resDict["success"]