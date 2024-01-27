import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

tick = "ES=F" #S&P 500 front-month futures ticker symbol
data = yf.download(tick)

sp500_data = pd.DataFrame(data)
sp500_data['Arithmetic returns'] = (sp500_data['Adj Close'] - sp500_data['Adj Close'].shift(1)) / sp500_data['Adj Close'].shift(1)
sp500_data['Log returns'] = np.log(sp500_data['Adj Close']/sp500_data['Adj Close'].shift(1))
#sp500_data['Log returns'] = np.log(sp500_data['Adj Close']).diff()
sp500_data.dropna(inplace=True)

plt.plot(sp500_data[['Log returns','Arithmetic returns']])
plt.title('SP500 Annual Arithmetic vs Logarithmic Returns')
plt.xlabel('Year')
plt.ylabel('Returns')
plt.legend(['Log returns','Arithmetic returns'],loc='upper right')
plt.grid(True)
plt.show()

sp500_data['Cumulative Arithmetic returns'] = sp500_data['Arithmetic returns'].cumsum()
sp500_data['Cumulative Log returns'] = np.exp(sp500_data['Log returns'].cumsum())-1

plt.plot(sp500_data[['Cumulative Log returns','Cumulative Arithmetic returns']])
plt.title('SP500 Cumulative Arithmetic vs Logarithmic Returns')
plt.xlabel('Year')
plt.ylabel('Cumulative Returns')
plt.legend(['Cumulative Log returns','Cumulative Arithmetic returns'],loc='upper right')
plt.grid(True)
plt.show()

# Exercice 1.9
annualized_log_return = sp500_data['Log returns'].mean() * 252