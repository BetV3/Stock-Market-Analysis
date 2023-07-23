import yfinance as yf
from yahoo_fin.stock_info import tickers_sp500
import os
root_path = os.getcwd()
print(root_path)


tickers = tickers_sp500()
with open('data/sp500.txt', 'w') as f:
    for ticker in tickers:
        print(ticker)
        f.write(ticker + '\n')