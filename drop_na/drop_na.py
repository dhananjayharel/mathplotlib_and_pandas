import pandas as pd
import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
from statistics import mean


def moving_average(data):
    return mean(data)

def fancy_this(data):
    return mean(data) + mean(data) + 5

style.use('fivethirtyeight')

start = datetime.datetime(2005, 1, 1)
end = datetime.datetime(2015, 1, 1)

att = web.DataReader("T", 'yahoo', start, end)
describe = att.describe()
#print(describe['Open']['std'])


att['50MA'] = att['Close'].rolling(50).mean()  
att['10MA'] = att['Close'].rolling(10).mean() 
att['50STD'] = att['Close'].rolling(50).std()
att['MA_with_apply'] = att['Close'].rolling(50).apply(moving_average)
att['apply'] = att['Close'].rolling(50).apply(fancy_this)

print(att.head())

#att.dropna(inplace=True)

att.dropna(how='all', inplace=True)
print(att.head())

