from matplotlib.dates import DateFormatter
import yfinance as yf
from pandas_datareader import data as pdr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

yf.pdr_override()

def sma(price, n):
    print()


Open = 'Open'
Close = 'Close'
High = 'High'
Low = 'Low'

fig = plt.figure()
ax = fig.add_subplot(111)



data = pdr.get_data_yahoo("SPY", start="2023-03-01", end="2023-03-26")
low_prices = pd.DataFrame({'low': data[Low]},index=data.index)
print(low_prices)
down = data[data.get('Close') >= data.get('Open')]
up = data[data.get('Close') < data.get('Open')]

downcolor = 'red'
upcolor = 'green'

width = .3
width2 = .03

#Graphing the Red Bars
ax.bar(down.index, down.get(Close)-down.get(Open), width=width, bottom=down.get(Open), color=downcolor)
ax.bar(down.index, down.get(High)-down.get(Close), width=width2, bottom=down.get(Close), color=downcolor)
ax.bar(down.index, down.get(Low)-down.get(Open), width2, bottom=down.get(Open), color=downcolor)

#Graphing the Green Bars
ax.bar(up.index, up.get(Close)-up.get(Open), width, bottom=up.get(Open), color=upcolor)
ax.bar(up.index, up.get(High)-up.get(Open), width2, bottom=up.get(Open), color=upcolor)
ax.bar(up.index, up.get(Low)-up.get(High), width2, bottom=up.get(Close), color=upcolor)

ax.set(xlabel='Date', ylabel='Price', title='Price for {}'.format("SPY"))

date_form = DateFormatter("%d")
ax.xaxis.set_major_formatter(date_form)

#plt.show()