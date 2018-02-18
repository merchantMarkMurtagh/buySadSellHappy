def prettyPrint(marketDict):
	for i in marketDict:
		print (i["MarketCurrencyLong"] + " | " + str(i["MinTradeSize"]))
