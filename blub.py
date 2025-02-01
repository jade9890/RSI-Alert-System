import pandas as pd
import yfinance as yf
import talib as ta
import matplotlib.pyplot as plt

# list of stocks 
tickers_list = ["SOXL", "SOXS", "UBER", "PDD", "JKS", "NVDA", "MU", "MSFT"]

#download the data of all stocks, 100 candles
data = yf.download(tickers_list, period="1mo", interval="1h", group_by='ticker')


close_prices = data.xs("Close", axis=1, level=1)

#dictionary to put data in
rsi_data={}

#loop through each ticker and get the RSI
for ticker in tickers_list:
    if ticker in close_prices:
        rsi_data[ticker] = ta.RSI(close_prices[ticker], timeperiod=14)

rsi_dataframe=pd.DataFrame(rsi_data)
print(rsi_dataframe.tail(1))

#def generate_rsi_signals(data, period=14, overbough_threshold=70,oversolv_threshold=30):
    #calculate RSI
    #initialize signal column with neutral
    #data['Signal'] = 'Neutral'

    
