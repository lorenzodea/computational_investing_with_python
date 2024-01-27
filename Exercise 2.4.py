import numpy as np
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

#Exercise 2.2

tick = "ES=F" #S&P 500 front-month futures ticker symbol
data = yf.download(tick)

sp500_data = pd.DataFrame(data)
sp500_data['Log returns'] = np.log(sp500_data['Adj Close']).diff()
sp500_data.dropna(inplace=True)

volatility = sp500_data['Log returns'].std()
mean_return = sp500_data['Log returns'].mean()
annualized_volatility = volatility * np.sqrt(252)

max_daily_return = np.round(sp500_data['Log returns'].max(),5)
min_daily_return = np.round(sp500_data['Log returns'].min(),5)
n_bins = int((max_daily_return-min_daily_return)*100)

plt.hist(sp500_data['Log returns'], bins=n_bins, label = 'Actual Distribution')
plt.axvline(mean_return, color ='black', linestyle = 'dashed', linewidth=2, label = 'Daily Mean return')
for i in range(1,4):    
     plt.axvline(mean_return+volatility*i, color ='green', linestyle = 'dashed', linewidth=1, label = f'+{i} std')
     plt.axvline(mean_return-volatility*i, color ='red', linestyle = 'dashed', linewidth=1, label = f'-{i} std')

plt.title('Histogram of SP500 Futures Logarithmic Returns')
plt.xlabel('Logarithmic Returns')
plt.ylabel('Frequency/Density')
plt.yscale("log")

plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))


plt.legend()
plt.show()