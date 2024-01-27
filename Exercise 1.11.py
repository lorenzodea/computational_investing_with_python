import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

tick = "ES=F" #S&P 500 front-month futures ticker symbol
data = yf.download(tick)

sp500_data = pd.DataFrame(data)
sp500_data['Log returns'] = np.log(sp500_data['Adj Close']).diff()
sp500_data.dropna(inplace=True)

max_daily_return = np.round(sp500_data['Log returns'].max(),2)
min_daily_return = np.round(sp500_data['Log returns'].min(),2)
n_bins = int((max_daily_return-min_daily_return)*100)

plt.hist(sp500_data['Log returns'], bins = n_bins, color='orange', label = 'Return Distribution')
plt.axvline(sp500_data['Log returns'].mean(), color ='black', linestyle = 'dashed', linewidth=2, label = 'Daily Mean return')
plt.title('Histogram of SP500 Futures Logarithmic Returns')
plt.xlabel('Logarithmic Returns')
plt.ylabel('Frequency (log)')
plt.yscale("log")
plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))

plt.legend()
plt.show()