import pandas as pd
import os
import json

sp500 = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")[0]
sp500['Symbol'] = sp500["Symbol"].str.replace(".", "-")
tickers = {}
for ticker in sp500["Symbol"]:
    print("saving this ticker: ", ticker)
    tickers[ticker] = sp500[ticker].tolist()
json.dumps(tickers)