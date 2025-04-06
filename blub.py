import pandas as pd
import yfinance as yf
import talib as ta
import telegram_send

TOKIN = '8099730414:AAEEmj7GBNFv_R6DGGcQlfbSCBKWRX74UjU'

import requests
url = 'https://telegram.me/Jades_rsi_bot'

# List of stocks 
tickers_list = ["SOXL", "SOXS", "UBER", "PDD", "JKS", "NVDA", "MU", "MSFT"]

# Download stock data in 1hr, 5min, and 90min intervals
oneHourData = yf.download(tickers_list, period="1mo", interval="1h", group_by='ticker')
fiveMinData = yf.download(tickers_list, period="1mo", interval="5m", group_by='ticker')
ninetyMinData = yf.download(tickers_list, period="1mo", interval="90m", group_by='ticker')

# Extract close prices for each timeframe
close_prices_5min = fiveMinData.xs("Close", axis=1, level=1)
close_prices_hour = oneHourData.xs("Close", axis=1, level=1)
close_prices_90min = ninetyMinData.xs("Close", axis=1, level=1)

# Calculate RSI for each timeframe
rsi_5min = pd.DataFrame({ticker: ta.RSI(close_prices_5min[ticker], timeperiod=14) for ticker in tickers_list})
rsi_90min = pd.DataFrame({ticker: ta.RSI(close_prices_90min[ticker], timeperiod=14) for ticker in tickers_list})
rsi_hour = pd.DataFrame({ticker: ta.RSI(close_prices_hour[ticker], timeperiod=14) for ticker in tickers_list})

# Combine all RSI data into a flat table
rsi_combined_flat = pd.DataFrame({
    '5min RSI': rsi_5min.iloc[-1],  # Most recent 5min RSI values
    '90min RSI': rsi_90min.iloc[-1],  # Most recent 90min RSI values
    '1hr RSI': rsi_hour.iloc[-1]  # Most recent 1hr RSI values
}).T  # Transpose to have tickers as rows

# Display the flat dataframe
print(rsi_combined_flat)


