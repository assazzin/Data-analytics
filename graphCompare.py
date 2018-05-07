import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df=df.drop(['DATE'], 1)

# Plot 2 graps for correlation comparing
stock1 = 'WHA'
stock2 = 'TCAP'

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(df[stock1], 'blue')
ax1.set_ylabel(stock1, color='blue')

ax2 = ax1.twinx()
ax2.plot(df[stock2], 'coral')
ax2.set_ylabel(stock2, color='coral')

ax1.set_xlabel('Days')
plt.show()
