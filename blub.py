import pandas as pd
import yfinance as yf
import talib as ta
import matplotlib.pyplot as plt

tickers_list= ["SOXL","SOXS","UBER","PDD","JKS","NVDA","MU"] # list of stocks I want to keep track of
tickers_data= {} # empty dictionary

