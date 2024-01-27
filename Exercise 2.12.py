import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

#Exercise 2.2

tick = "ES=F" #S&P 500 front-month futures ticker symbol
data = yf.download(tick)

sp500_data = pd.DataFrame(data)
sp500_data['Log returns'] = np.log(sp500_data['Adj Close']).diff()
sp500_data.dropna(inplace=True)

sp500_data['Cumulative Log returns'] = np.exp(sp500_data['Log returns'].cumsum())-1
rolling_max = sp500_data['Cumulative Log returns'].cummax()
sp500_data['Drawdown'] = rolling_max - sp500_data['Cumulative Log returns']

fig, ax = plt.subplots()
ax.fill_between(sp500_data.index, sp500_data['Drawdown'], color='red',alpha=0.3)
ax.plot(sp500_data['Cumulative Log returns'],label='Cumulative returns')
ax.set_title('Cumulative returns and ongoing Drawdown')
ax.set_xlabel('Date')
ax.set_ylabel('Returns/Drawdown')
ax.legend()
plt.show()