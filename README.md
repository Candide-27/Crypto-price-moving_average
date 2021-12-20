# Crypto-price-moving_average
Tracking (of choice) cryptocurrencies' daily prices and moving average.

## About Alpha Vantage
The Alpha Vantage library (https://www.alphavantage.co/documentation/) allows tracking the price movement of stocks, cryptocurriencies or economic indicators like real GDP. This python script uses Alpha Vantage's free API to retrieve 4 endogeneous cryptocurriencies' closing prices. Much as Alpha Vantage has an extremely useful TechIndicators function to calculate the eponymous tasks such as simple moving average and exponential moving, etc., they are applicable only to stocks tickers and not cryptocurrencies symbols (or they could be but not that I am fully aware of). Therefore, in the script I also writes a basic simple moving average (SMA) function that takes in the user's Pandas series, interval of observation and period-to-average-over, to calculate the simple moivng average of a given time series. The SMA formula can be found on Investopedia (https://www.investopedia.com/terms/s/sma.asp). I then use that function to calculate the simple moving average of the crypto prices retrieved from Alpha Vantage API.

## Expected Outcome
The script produces a figure of 4 panels (2x2) of 4 chosen cryptocurrencies available at Alpha Vantage API. The API free key enables only 5 calls per minute, and I choose 4 for the sake of presentation. Each panel depicts the chosen cryptocurrency prices for the last k days and its moving average over n days, with k, n being chosen at the user's discretion. Then, an Excel sheet will also be generated, with each out of 4 sheets contain all the prices and moving average for the chosen cryptocurrency. The original script selects 4 cryptocurrencies: Bitcoin, Ether, Litecoin and Cardano. The user can change the desirable currencies names and symbols in the dictionary 'symbols_dict' at the beginning of the script.

![alt text](https://imgur.com/gallery/NvP8hLO)

## Remarks and criticism welcome. 
