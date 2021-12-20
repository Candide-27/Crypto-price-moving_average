import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
from alpha_vantage.cryptocurrencies import CryptoCurrencies

#Get API key for free at: https://www.alphavantage.co/support/#api-key
api = ''

symbols_dict = {'Bitcoin':'BTC', 'Ether':'ETH', 'Litecoin':'LTC', 'Cardano':'ADA'} #list of available currecncy: https://www.alphavantage.co/digital_currency_list/
key_list = list(symbols_dict)

#Parameters
obs = 100 #How many days of observation
period = 30 #How many days to average over
market = 'USD' #list of available market: https://www.alphavantage.co/physical_currency_list/
today = dt.date.today()
title = f'Cryptocurrencies\' prices (in {market}) over the last {obs} days, {today}'

#Graph parameters
plt.style.use('bmh')
params = {'figure.figsize' : (12,6),
          'axes.titlesize' : 10,
          'xtick.labelsize' : 6,
          'ytick.labelsize' : 9,
}
pylab.rcParams.update(params)

#excelwriter object
w = pd.ExcelWriter(f'{title}.xlsx', engine='xlsxwriter') #pip install xlsxwriter, xlwt

#cryptocurrencies object
cc = CryptoCurrencies(key=api, output_format='pandas')

#SMA function
def crypto_sma(series, obs, period):
    #use list comprehension to create a pandas series of moving average.
    result_sma = pd.Series([round(series.iloc[x:x+period].mean(),2) for x in range(0, series.iloc[:obs].shape[0])], index=series.iloc[:obs].index, name='SMA')
    return result_sma

#Create dataframe for every cryptocurrency in the dictionary: prices + sma
for k in range(len(key_list)):
    key_list[k], _ = cc.get_digital_currency_daily(symbol=symbols_dict.get(key_list[k]), market=market)
    key_list[k] = key_list[k].iloc[:,6] #retain only the 4a. close column
    key_list[k] = pd.concat([key_list[k], crypto_sma(key_list[k], obs, period)], axis=1, join='inner') #create SMA series & join using the intersection index

#Draw graph & create excel sheet
fig, ax = plt.subplots(2,2, sharex=True)
j = 0
#first while loop create ax[0,0] with key_list[0] and ax[1,0] with key_list[1]. Second while loop create ax[0,1] with key_list[2] and ax[1,1] with key_list[3].
while j < len(symbols_dict)//2:
    for i in range(len(symbols_dict)//2):
        ax[i,j].plot(key_list[i+j*2].index, key_list[i+j*2].iloc[:,0], label='Closing Price')
        ax[i,j].plot(key_list[i+j*2].index, key_list[i+j*2].iloc[:,1], label='Moving Average')
        ax[i,j].set_title([k for k in symbols_dict.keys()][i+j*2]) #list comprenhesionize all keys, then subscript the specific one currently in use in the loop.
        hdl, lbl = ax[i,j].get_legend_handles_labels() #elicit handles and labels from the axes
        key_list[i+j*2].to_excel(w, sheet_name=[k for k in symbols_dict.keys()][i+j*2]) #write dataframe to an excel sheet with corresponding crypto name.
    j += 1
fig.legend(hdl, lbl, loc='upper left')
fig.suptitle(title)
plt.show()

#Save the figure and the excel sheet
fig.savefig(f'{title}.jpg')
w.save()
