import numpy as np
import numpy as np
import matplotlib.pyplot as plt
 
# generating time series price data
mu = 0.001
sigma = 0.01
start_price = 5
np.random.seed(0)
returns = np.random.normal(loc=mu, scale=sigma, size=100)
price = start_price*(1+returns).cumprod()
 
# Simple Moving Averages 
window_size = 3
i = 0
# Initialize an empty list to store moving averages
moving_averages = []
 
#consider every window of size 3
while i < len(price) - window_size + 1:
    # Calculate the average of current window
   window_average = round(np.sum(price[
     i:i+window_size]) / window_size, 2)
    
   # Store the average of current
   # window in moving average list
   moving_averages.append(window_average)
    
   # Shift window to right by one position
   i += 1
 
# Plotting the SMA graph
plt.plot(price)
plt.plot(moving_averages)
# naming the x axis
plt.xlabel('Price')
# naming the y axis
plt.ylabel('SMA')
# giving a title to my graph
plt.title('SMA graph')
# function to show the plot
plt.show()
