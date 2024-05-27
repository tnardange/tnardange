import json
import urllib.request
import random
import QUERY



def getDataPoint(quote):
    stock=quote['stock']
    bid_price=float(quote['top_bid']['price'])
    ask_price=float(quote['top_ask']['price'])
    price=(bid_price + ask_price)/2
    return stock,bid_price,ask_price,price


def getRatio(price_a,price_b):
    if(price_b==0):
        return None
    return price_a/price_b


if __name__ == "__main__":
    N = 10
    for _ in range(N):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        prices = {}
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            prices[stock] = price
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
            
        if "ABC" in prices and "DEF" in prices:
            ratio = getRatio(prices["ABC"], prices["DEF"])
            if ratio is not None:
                print("Ratio %s" % ratio)
            else:
                print("Unable to compute ratio because one of the prices is zero.")
        else:
            print("Unable to compute ratio because one of the stocks (ABC or DEF) is missing.")
