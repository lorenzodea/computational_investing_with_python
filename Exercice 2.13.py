import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from scipy.stats import kurtosis, skew

sp500_futures = yf.download('ES=F')['Adj Close']
treasury_futures = yf.download('ZN=F')['Adj Close']

mydata = pd.DataFrame({
    'SP500': sp500_futures,
    'Treasury':treasury_futures})

mydata.dropna(inplace=True)


mydata['Log return SP500'] = np.log(mydata['SP500']).diff()
mydata['Log return Treasury'] = np.log(mydata['Treasury']).diff()
mydata.dropna(inplace=True)


mydata['Portfolio returns'] = 0.6 * mydata['Log return SP500'] + 0.4 * mydata['Log return Treasury']
mydata['Cumulative returns'] = np.exp(mydata['Portfolio returns'].cumsum())-1
mydata_rolling_max = mydata['Cumulative returns'].cummax()
mydata['Drawdown'] = mydata_rolling_max - mydata['Cumulative returns']

fig, ax = plt.subplots()
ax.fill_between(mydata.index, mydata['Drawdown'], color='red',alpha=0.3)
ax.plot(mydata['Cumulative returns'],label='Cumulative returns')
ax.set_title('Cumulative returns and ongoing Drawdown 60% SP500 40% TREASURY')
ax.set_xlabel('Date')
ax.set_ylabel('Returns/Drawdown')
ax.legend()
plt.show()

print(mydata['Drawdown'].max())

volatility = mydata['Portfolio returns'].std()
mean_return = mydata['Portfolio returns'].mean()
annualized_volatility = volatility * np.sqrt(252)

annualized_log_return = mean_return * 252
print(annualized_log_return)

deviation = mydata['Portfolio returns'] - mean_return
cubed_average = np.sum(deviation**3)/len(mydata['Portfolio returns'])
skewness= cubed_average/volatility**3
print(skewness)
print(skew(mydata['Portfolio returns']))

fourth_power_average = np.sum(deviation**4)/len(mydata['Portfolio returns'])
Kurtosis = fourth_power_average / volatility**4
print(Kurtosis)
print(kurtosis(mydata['Portfolio returns'])) #to compare to my kurtosis - 3