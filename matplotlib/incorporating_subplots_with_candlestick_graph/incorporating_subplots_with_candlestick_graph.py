import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import urllib
import numpy as np
import datetime as dt

from matplotlib import style

style.use('fivethirtyeight')

print(plt.style.available)

print(plt.__file__)


def bytespdate2num(fmt, encoding='utf-8'):
    str_converter = mdates.strpdate2num(fmt)
    def bytes_converter(b):
        s = b.decode(encoding)
        return str_converter(s)
    return bytes_converter

def graph_data(stock):

    fig = plt.figure()
    
    ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
    ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1)
    plt.ylabel('Price')
    ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)

    
    print('Currently pulling:', stock)
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=3m/csv'
    print(url)
    source_code = urllib.request.urlopen(url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')

    for each_line in split_source:
        split_line = each_line.split(',')
        if len(split_line) == 6:
            if 'values' not in each_line:
                stock_data.append(each_line)

    
    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data, delimiter = ',',
                                                          unpack = True,
                                                          converters={0: bytespdate2num('%Y%m%d')})


    x = 0
    y = len(date)

    new_list = []
    while x < y:
        append_line = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        new_list.append(append_line)
        x += 1

        
    
    candlestick_ohlc(ax2, new_list, width=.6, colorup='#41ad49', colordown='#ff1717')
    ax2.grid(True)#, color = 'g', linestyle='-', linewidth=3)
    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)
    ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))


    bbox_props = dict(boxstyle='round4, pad=0.3', fc="y", ec='k', lw=2)
    ax2.annotate(str(closep[-1]), (date[-1], closep[-1]),
                 xytext = (date[-1]+8, closep[-1]), bbox = bbox_props)



        
    plt.subplots_adjust(left=.11, bottom=.16, right=.90, top=.95, wspace=.2, hspace=.2)
    plt.show()



stock = input('Stock to plot: ')
graph_data(stock)
