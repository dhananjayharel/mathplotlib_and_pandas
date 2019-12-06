import pandas as pd
import pandas_datareader as web
import datetime

import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 1, 1)

att = web.DataReader("T", 'yahoo', start, end)
describe = att.describe()
#print(describe['Open']['std'])

att['50MA'] = att['Close'].rolling(50).mean()
att['10MA'] = att['Close'].rolling(10).mean()
#print(att.tail())

fig, axes = plt.subplots(nrows=2, ncols=1)

att['50STD'] = att['Close'].rolling(50).std()
att['50STD'].plot(ax=axes[1], label='50STD')

att['Close'].plot(ax=axes[0], label='Price')
att['50MA'].plot(ax=axes[0], label='50MA')
att['10MA'].plot(ax=axes[0], label='10MA')
plt.legend(loc=4)

plt.show()
plt.savefig('plot.png')