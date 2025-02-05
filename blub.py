import pandas as pd
import yfinance as yf
import talib as ta
import matplotlib.pyplot as plt

# list of stocks 
tickers_list = ["SOXL", "SOXS", "UBER", "PDD", "JKS", "NVDA", "MU", "MSFT"]

#download stock data in 1hr, 3min, and 4hr intervals
oneHourData = yf.download(tickers_list, period="1mo", interval="1h", group_by='ticker')
fiveMinData = yf.download(tickers_list, period="1mo", interval="5m", group_by='ticker')
ninetyMinData = yf.download(tickers_list, period="1mo", interval="90m", group_by='ticker')

oneHourData.index = oneHourData.index.tz_localize(None)
fiveMinData.index = fiveMinData.index.tz_localize(None)
ninetyMinData.index = ninetyMinData.index.tz_localize(None)


close_prices_5min = fiveMinData.xs("Close", axis=1, level=1)
close_prices_hour = oneHourData.xs("Close", axis=1, level=1)
close_prices_90min = ninetyMinData.xs("Close", axis=1, level=1)

timeframes = {
    "1h": close_prices_hour,
    "5m": close_prices_5min,
    "90m": close_prices_90min
}
#dictionary to put data in
rsi_data={}

#loop through each ticker and get the RSI
for timeframe, close_price_df in timeframes.items():
    for ticker in tickers_list:
        if ticker in close_price_df.columns:
            rsi_data[(ticker, timeframe)] = ta.RSI(close_price_df[ticker], timeperiod=14)

rsi_dataframe=pd.DataFrame(rsi_data)
print(rsi_dataframe.tail(10))




    
