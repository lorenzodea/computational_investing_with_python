import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
from scipy.stats import norm, kurtosis, skew

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
n_bins = int((max_daily_return-min_daily_return)*10000)
norm_dist = np.linspace(min_daily_return, max_daily_return,n_bins)
norm_curve = norm.pdf(norm_dist,mean_return,volatility)

plt.hist(sp500_data['Log returns'], bins=n_bins, color='orange', label = 'Actual Distribution')
plt.plot(norm_dist,norm_curve,color='red', label = 'Normal distribution')

plt.axvline(mean_return, color ='black', linestyle = 'dashed', linewidth=2, label = 'Daily Mean return')
for i in range(1,4):    
    plt.axvline(mean_return+volatility*i, color ='green', linestyle = 'dashed', linewidth=1, label = f'+{i} std')
    plt.axvline(mean_return-volatility*i, color ='red', linestyle = 'dashed', linewidth=1, label = f'-{i} std')


plt.title('Histogram of SP500 Futures Logarithmic Returns')
plt.xlabel('Logarithmic Returns')
plt.ylabel('Frequency/Density')

plt.legend()
plt.show()

annualized_log_return = sp500_data['Log returns'].mean() * 252
print(annualized_log_return)

deviation = sp500_data['Log returns'] - mean_return
cubed_average = np.sum(deviation**3)/len(sp500_data['Log returns'])
skewness= cubed_average/volatility**3
print(skewness)
print(skew(sp500_data['Log returns']))

fourth_power_average = np.sum(deviation**4)/len(sp500_data['Log returns'])
Kurtosis = fourth_power_average / volatility**4
print(Kurtosis)
print(kurtosis(sp500_data['Log returns'])) #to compare to my kurtosis - 3
