__author__ = 'Suota'

import csv ,numpy as np
from datetime import date
import wget ,matplotlib.pyplot as plt

fb_url = 'http://www.google.com/finance/historical?q=NASDAQ%3AFB&ei=7qI_VpHLAYLGsAHBioqYBA&output=csv'
tw_url = 'http://www.google.com/finance/historical?q=NYSE%3ATWTR&ei=fqQ_VtmpLpPjsgGL2Y2YCA&output=csv'
goo_url = 'http://www.google.com/finance/historical?q=NASDAQ%3AGOOG&ei=oqQ_VojzOoLGsAHBioqYBA&output=csv'
ms_url = 'http://www.google.com/finance/historical?q=NASDAQ%3AMSFT&ei=2aQ_VvDjGMqosgGSg4bYCw&output=csv'

comp_url = (fb_url, goo_url, ms_url,tw_url )
filename = ('fb.csv' , 'goog.csv', 'msft.csv' , 'twtr.csv')
label_name = ("Facebook", "Google" , "Microsoft" , "Twitter")

today = date.today()
plt_set = False
fig = plt.figure(figsize=(10,4))
one_month = False
one_week = False


def set_fb():
    set_plt(0)


def set_goog():
    set_plt(1)


def set_ms():
    set_plt(2)


def set_tw():
    set_plt(3)


def set_plt(id):
    global plt_set
    plt_set = True

    wget.download(comp_url[id]) # downloading data from google.com about one of companies' share price as .csv

    with open(filename[id], newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        global row_count
        row_count = sum(1 for row in csvreader)  # counting number of rows in file

    if one_month:
        row_count = 31
    if one_week:
        row_count = 7
    time = ()
    text_formatted = []
    time=range(1,row_count)

    text_formatted = np.genfromtxt(filename[id], delimiter=',', skip_header=1,
                      names=['x', 'y'])

# plotting share prices of choosed company

    ax1 = fig.add_subplot(122)
    ax1.set_title(label_name[id])
    ax1.set_xlabel('time [days ago] ')
    ax1.set_ylabel('Prices[USD]')

    if one_month :
        ax1.plot(time, text_formatted['y'][:30], color='r', label='the data')
    elif one_week :
         ax1.plot(time, text_formatted['y'][:6], color='r', label='the data')
    else:
        ax1.plot(time, text_formatted['y'], color='r', label='the data')

    plt.show()


def month():
    global one_month
    one_month = True


def week():
    global one_week
    one_week = True
