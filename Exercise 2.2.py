import numpy as np
import yfinance as yf
import pandas as pd


tick = "ES=F" #S&P 500 front-month futures ticker symbol
data = yf.download(tick)

sp500_data = pd.DataFrame(data)
sp500_data['Log returns'] = np.log(sp500_data['Adj Close']).diff()

volatility = sp500_data['Log returns'].std()
mean_return = sp500_data['Log returns'].mean()
annualized_volatility = volatility * np.sqrt(252)
print(annualized_volatility)
