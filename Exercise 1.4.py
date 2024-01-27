import numpy as np
import matplotlib.pyplot as plt

values = np.array([10,12.5,8,13.5,7.5,15])

arithmetic_returns =  (values[1:] - values[:-1]) / values[:-1]
log_returns = np.log(values[1:]/values[:-1])


plt.plot(arithmetic_returns, label='Arithmetic Returns', marker ='o')
plt.plot(log_returns, label='Logarithmic Returns', marker ='x')
plt.title('Annual Arithmetic vs Logarithmic Returns')
plt.xlabel('Year')
plt.ylabel('Returns')
plt.legend()
plt.grid(True)
plt.show()

cumulative_arithmetic_returns = np.cumsum(arithmetic_returns)
#np.sum((values[1:]-values[:-1])/values[:-1])
cumulative_log_returns = np.exp(np.cumsum(log_returns))-1

plt.plot(cumulative_arithmetic_returns, label='Cumulative Arithmetic Returns', marker ='o')
plt.plot(cumulative_log_returns, label='Cumulative Logarithmic Returns', marker ='x')
plt.title('Cumulative Arithmetic vs Logarithmic Returns')
plt.xlabel('Year')
plt.ylabel('Cumulative Returns')
plt.legend()
plt.grid(True)
plt.show()