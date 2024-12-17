import yfinance as yf
import pandas as pd
import numpy as np
tickers = ['AAPL', 'MSFT', 'GOOGL']
data = yf.download(tickers, start='2023-01-01', end='2024-01-01')['Adj Close']
daily_returns = data.pct_change()
weights = np.array([0.33,0.33,0.34])
portfolio_returns = daily_returns.dot(weights)
portfolio_daily_return = portfolio_returns.sum()
print("portfolio return:")
print(portfolio_daily_return)