import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def fetch(ticker, start="2023-01-01", end="2024-01-01", interval="1d"):
    data = yf.download(tickers=ticker, start=start, end=end, interval=interval)
    return data
ticker = input("Enter the ticker symbol :")
data = fetch(ticker)
data
plt.plot(data.index, data["Adj Close"])
plt.ylabel("Stock Price")
plt.xlabel("Date")
plt.title("Apple’s stock price over the past year")
plt.show()


#The graph shows apple's stock price over the past one year. The stock's price showed a significant upward trend as the year started till around the month of august. Then the market showed a slight downward trend till november and consecutively, the stock's prices rose again till December to reach the previous high they had occurred till august